__author__ = 'jszheng'

# 在类的创立(注意不是类实例的创立)加修饰
# 元类是Type的子类, 跟ruby一样
# class 类名(超类名): ...
# 等效于创建type实例
# class = type(类名, 超类名, 属性dict)
#   调用type.__new__
#   调用type.__init__


# 定义元类
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new', classname, supers, classdict)
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In MetaOne.init', classname, supers, classdict)
        print('...init class object:', list(Class.__dict__.keys()))


# 定义meta function, 即为工厂函数
def MetaFunc(classname, supers, classdict):
    print('In MetaFunc', classname, supers, classdict)
    return type(classname, supers, classdict)


class Eggs:
    pass


class Meat:
    pass

print('Makeing Class')


class Spam(Eggs, Meat, metaclass=MetaOne):
    data = 1
    def meth(self, arg):
        pass

print('Makeinig Instance')
X = Spam()
print('data: ', X.data)


class Spam2(Eggs, Meat, metaclass=MetaFunc):
    data = 1
    def meth(self, arg):
        pass

print('Makeinig Instance')
X = Spam2()
print('data: ', X.data)


class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print(' In SuperMeta. call: ', classname, supers, classdict, sep=' \n. . . ')
        return type.__call__(meta, classname, supers, classdict)


class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print(' In SubMeta. new: ', classname, supers, classdict, sep=' \n. . . ')
        return type.__new__(meta, classname, supers, classdict)


    def __init__(Class, classname, supers, classdict):
        print(' In SubMeta init: ', classname, supers, classdict, sep=' \n. . . ')
        print(' . . . init class obj ect: ', list(Class.__dict__.keys()))


print(' making class')


class Spam3(Eggs, metaclass=SubMeta):
    data = 1

    def meth(self, arg):
        pass


print(' making instance')
X = Spam3()
print(' data: ', X.data)