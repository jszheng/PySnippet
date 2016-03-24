import os
import re
import shutil


def ord2chr(m):
    ch = chr(int(m.group(1), 16))
    if ch == ':' or ch == '/':
        ch = ' '
    return ch


def process_filename(dirname):
    espat = re.compile(r'%(\d\d)')
    count = 0
    for f in os.listdir(dirname):
        fnew = espat.sub(ord2chr, f)
        if f != fnew:
            src = os.path.join(dirname, f)
            dst = os.path.join(dirname, fnew)
            print(src, " => ", dst)
            shutil.move(src, dst)
            count += 1
    print('Total', count, 'files renamed.')


if __name__ == '__main__':
    process_filename('.')
