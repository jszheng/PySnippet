__author__ = 'jszheng'

# 就是修饰器. decorator

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args, **kwargs)


class Parrot:
    def __init__(self):
        self._voltage = 1000

    @property
    def voltage(self):
        """get current voltage"""
        return self._voltage

    @voltage.setter
    def voltage(self, new_value):
        self._voltage = new_value

if __name__ == '__main__':
    # 调用了类的构造函数,返回一个对象记录了下面函数的信息
    # 用该对象重命名了spam
    # 当调用spam函数时候实际上是调用对象的__call__
    @tracer
    def spam(a, b, c):
        print(a, b, c)

    spam(1, 2, 3)
    spam(4, 5, 6)
    spam(7, 8, 9)

    p = Parrot()
    print(p.voltage)
    print(type(p))
    print(dir(p))
    print(p.__class__)
    p.voltage = 12
    print(p.voltage)
    print(dir(p))