__author__ = 'jszheng'


# 一个可以用于类中实例方法的修饰器的写法
# 传入原来的函数(即将被修饰的函数), 做一些自己想做的事情后再call他.
def tracer(func):
    calls = 0
    # 立即定义一个callable返回
    # 计数是一个局部变量,不同包装的函数有自己的计数器
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall


# 用描述符类的方式会困难些因为self传入的麻烦
# 不建议使用
class decr_tracer:
    def __init__(self, func):
        self.calls = 0  # 调用的次数
        self.func = func  # 调用的函数(或是实例方法) 注意这里没有实例本身的应用.

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        print('get ', self, instance, owner)
        # 调用函数前会落到这里来获取函数名
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)
            # 这里的self是tracer的实例, 会导致调用 __call__
            # 而传入的第一个参数就是被包裹的实例
        return wrapper  #将局部函数返回



if __name__ == '__main__':
    @tracer
    def spam(a, b, c):
        print(a + b + c)

    spam(1, 2, 3)
    spam(a=4, c=6, b=5)

    class Person:
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay

        @tracer
        def give_raise(self, percent):
            self.pay *= 1.0 + percent

        @decr_tracer
        def last_name(self):
            return self.name.split()[-1]

    print('methods...')
    bob = Person('Bob Smith', 5000)
    sue = Person('Sue Jones', 10000)
    print(bob.name)
    sue.give_raise(.10)
    print(sue.pay)
    print(bob.last_name())
    print(sue.last_name())

    # 在call bob.last_name()函数时发生了什么
    # 1. __get__(<decr_tracer object> <Person object> <class Person'> 去获取last_name函数名
    #    其中定义了一个wrapper函数将对他的调用转换为<decr_tracer object>的__call__调用
    #    但是传入的self却是bob实例, 形成一个closure包返回
    # 2. 调用该wrapper函数
    # 3. 转而调用<decr_tracer object>.__call__(bob, ...)
    #    增加计数器
    #    打印信息
    #    调用bob.last_name(), 注意__call__得到的self就是bob, 而不是<decr_tracer object>实例