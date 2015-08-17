#! /usr/bin/python
# -*- coding: utf-8

import re

terminal_escape = re.compile('(\001?\033\\[[0-9;]*m\002?)')
escape_parts = re.compile('\001?\033\\[([0-9;]*)m\002?')


class AnsiState(object):
    def __init__(self, bold=False, inverse=False, color="white", background="black", backgroundbold=False):
        self.bold = bold
        self.inverse = inverse
        self.color = color
        self.background = background
        self.backgroundbold = backgroundbold

    trtable = {"black": 0, "red": 4, "green": 2, "yellow": 6,
               "blue": 1, "magenta": 5, "cyan": 3, "white": 7}
    revtable = dict(zip(trtable.values(), trtable.keys()))

    def get_winattr(self):
        attr = 0
        if self.bold:
            attr |= 0x0008
        if self.backgroundbold:
            attr |= 0x0080
        if self.inverse:
            attr |= 0x4000
        attr |= self.trtable[self.color]
        attr |= (self.trtable[self.background] << 4)
        return attr

    def set_winattr(self, attr):
        self.bold = bool(attr & 0x0008)
        self.backgroundbold = bool(attr & 0x0080)
        self.inverse = bool(attr & 0x4000)
        self.color = self.revtable[attr & 0x0007]
        self.background = self.revtable[(attr & 0x0070) >> 4]

    winattr = property(get_winattr, set_winattr)

    def __repr__(self):
        return 'AnsiState(bold=%s,inverse=%s,color=%9s,' \
               'background=%9s,backgroundbold=%s)# 0x%x' % \
               (self.bold, self.inverse, '"%s"' % self.color,
                '"%s"' % self.background, self.backgroundbold,
                self.winattr)

    def copy(self):
        x = AnsiState()
        x.bold = self.bold
        x.inverse = self.inverse
        x.color = self.color
        x.background = self.background
        x.backgroundbold = self.backgroundbold
        return x


defaultstate = AnsiState(False, False, "white")

trtable = {0: "black", 1: "red", 2: "green", 3: "yellow",
           4: "blue", 5: "magenta", 6: "cyan", 7: "white"}


class AnsiWriter(object):
    def __init__(self, default=defaultstate):
        if isinstance(defaultstate, AnsiState):
            self.defaultstate = default
        else:
            self.defaultstate = AnsiState()
            self.defaultstate.winattr = defaultstate

    def write_color(self, text, attr=None):
        """write text at current cursor position and interpret color escapes.

        return the number of characters written.
        """
        if isinstance(attr, AnsiState):
            defaultstate = attr
        elif attr is None:  # use attribute form initial console
            attr = self.defaultstate.copy()
        else:
            defaultstate = AnsiState()
            defaultstate.winattr = attr
            attr = defaultstate
        chunks = terminal_escape.split(text)
        n = 0  # count the characters we actually write, omitting the escapes
        res = []
        for chunk in chunks:
            m = escape_parts.match(chunk)
            if m:
                parts = m.group(1).split(";")
                if len(parts) == 1 and parts[0] == "0":
                    attr = self.defaultstate.copy()
                    continue
                for part in parts:
                    if part == "0":  # No text attribute
                        attr = self.defaultstate.copy()
                        attr.bold = False
                    elif part == "7":  # switch on reverse
                        attr.inverse = True
                    elif part == "1":  # switch on bold (i.e. intensify foreground color)
                        attr.bold = True
                    elif len(part) == 2 and "30" <= part <= "37":  # set foreground color
                        attr.color = trtable[int(part) - 30]
                    elif len(part) == 2 and "40" <= part <= "47":  # set background color
                        attr.backgroundcolor = trtable[int(part) - 40]
                continue
            n += len(chunk)
            if True:
                res.append((attr.copy(), chunk))
        return n, res

    def parse_color(self, text, attr=None):
        n, res = self.write_color(text, attr)
        return n, [attr.winattr for attr, text in res]


def write_color(text, attr=None):
    a = AnsiWriter(defaultstate)
    return a.write_color(text, attr)


STYLE = {
    'fore': {
        'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
        'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37,
    },
    'back': {
        'black': 40, 'red': 41, 'green': 42, 'yellow': 43,
        'blue': 44, 'purple': 45, 'cyan': 46, 'white': 47,
    },
    'mode': {
        'bold': 1, 'underline': 4, 'blink': 5, 'invert': 7,
    },
    'default': {
        'end': 0,
    }
}


def use_style(string, mode='', fore='', back=''):
    mode = '%s' % STYLE['mode'][mode] if (mode in STYLE['mode']) else ''
    fore = '%s' % STYLE['fore'][fore] if (fore in STYLE['fore']) else ''
    back = '%s' % STYLE['back'][back] if (back in STYLE['back']) else ''
    style = ';'.join([s for s in [mode, fore, back] if s])
    style = '\033[%sm' % style if style else ''
    end = '\033[%sm' % STYLE['default']['end'] if style else ''
    return '%s%s%s' % (style, string, end)


def test():
    print(use_style('Normal'))
    print(use_style('Bold', mode='bold'))
    print(use_style('Underline & red text', mode='underline', fore='red'))
    print(use_style('Invert & green back', mode='reverse', back='green'))
    print(use_style('Black text & White back', fore='black', back='white'))


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"


def disable():
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''


def infog(msg):
    print(OKGREEN + msg + ENDC)


def info(msg):
    print(OKBLUE + msg + ENDC)


def warn(msg):
    print(WARNING + msg + ENDC)


def err(msg):
    print(FAIL + msg + ENDC)


if __name__ == '__main__':
    import pprint

    pprint = pprint.pprint

    s = "\033[0;31mred\033[0;32mgreen\033[0;33myellow\033[0;34mblue\033[0;35mmagenta\033[0;36mcyan\033[0;37mwhite\033[0m"
    ret = write_color(s)
    print(type(ret))

    test()
    print_format_table()
    info("Hello World")
    err("System Error")


"""
===================================
ANSI控制码的说明
33[0m 关闭所有属性
33[1m 设置高亮度
33[4m 下划线
33[5m 闪烁
33[7m 反显
33[8m 消隐
33[30m -- 33[37m 设置前景色
33[40m -- 33[47m 设置背景色
33[nA 光标上移n行
33[nB 光标下移n行
33[nC 光标右移n行
33[nD 光标左移n行
33[y;xH设置光标位置
33[2J 清屏
33[K 清除从光标到行尾的内容
33[s 保存光标位置
33[u 恢复光标位置
33[?25l 隐藏光标
33[?25h 显示光标

https://en.wikipedia.org/wiki/ANSI_escape_code

ESC [ 0 m       # reset all (colors and brightness)
ESC [ 1 m       # bright
ESC [ 2 m       # dim (looks same as normal brightness)
ESC [ 22 m      # normal brightness

# FOREGROUND:
ESC [ 30 m      # black
ESC [ 31 m      # red
ESC [ 32 m      # green
ESC [ 33 m      # yellow
ESC [ 34 m      # blue
ESC [ 35 m      # magenta
ESC [ 36 m      # cyan
ESC [ 37 m      # white
ESC [ 39 m      # reset

# BACKGROUND
ESC [ 40 m      # black
ESC [ 41 m      # red
ESC [ 42 m      # green
ESC [ 43 m      # yellow
ESC [ 44 m      # blue
ESC [ 45 m      # magenta
ESC [ 46 m      # cyan
ESC [ 47 m      # white
ESC [ 49 m      # reset

# cursor positioning
ESC [ y;x H     # position cursor at x across, y down

# clear the screen
ESC [ mode J    # clear the screen. Only mode 2 (clear entire screen)
                # is supported. It should be easy to add other modes,
                # let me know if that would be useful.
"""