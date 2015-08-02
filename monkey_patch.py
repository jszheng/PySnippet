def foo():
    print('foo')


class A:
    def bar(self):
        print('bar')

#独立的方法和类
a = A()
print(foo)
print(a.bar)


# 准备加入类中的方法需带有第一个参数，名字不一定叫self
def fooFighter(self):
    print('fooFighter', self)
# 加入类成为实例方法，同样可以被前面定义的a实例在后面调用
A.fooFighter = fooFighter  #  <<<<<<<<<<<<
a2 = A()
print(a2.fooFighter)
#可以调用了
a2.fooFighter()
a.fooFighter()


# 如何只加入一个实例中
import types
def fooInstance(self):
    print('fooInstance')
a3 = A()
a3.fooInstance = types.MethodType(fooInstance, a3)
print(a3.fooInstance)
a3.fooInstance()
print(dir(a))
print(dir(a2))
print(dir(a3))


# summary usage
def a_method(target, arg1):
    print('arg1=', arg1)
    print('called from', target)


def patch_me(target, method):
    # 注意这里将实例函数名定义为跟传入的函数名不一样！
    target.method = types.MethodType(method, target)


class B:
    pass

b = B()

patch_me(b, a_method)
b.method(3)

patch_me(B, a_method)
B.method(4)

b1 = B()
print(dir(b1))
print(b1.method)
b1.method(5)  # 这里调用的不是实例函数