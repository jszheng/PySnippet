class MyClass:
    def imeth(self, x):
        print(self, x)

    def smeth(x):
        print(x)

    def cmeth(cls, x):
        print(cls, x)

    asmeth = staticmethod(smeth)
    acmeth = classmethod(cmeth)

if __name__ == '__main__':
    obj = MyClass()
    obj.imeth(1)            # 通常的实例调用方法
    MyClass.imeth(obj, 2)   # 等效于

    MyClass.smeth(3)        # 通常的静态方法调用
    MyClass.asmeth(3)       # 也可以用
    obj.asmeth(2)           # 通过obj找到类静态方法
                            # 不允许obj.smeth
    print(dir(obj))         # 看看在dict中吗
    print(obj.__dict__)

    MyClass.acmeth(5)       # 通常的类方法调用, 传入了类
                            # 不允许MyClass.cmeth(5)

    obj.cmeth(6)            # 被转换会cmeth(obj, 6)
    obj.acmeth(6)           # 被转换会cmeth(MyClass, 6)