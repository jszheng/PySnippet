__author__ = 'jszheng'

# 所有python的方法就是一个描述符的实现. 任何method就是对象的一种特殊属性,可用被调用的属性.
# def定义的方法(函数或是lambda)默认是一个描述符, 除了拥有__call__实现外还有__get__, __set__, __delete__实现
# 没有绑定的描述符没有意义, 当绑定到类上后就有self参数了.
# <i>.<m>() -> <c>.__dict__['<m>'].__get__(<i>, <c>)


# 描述符是一个类, 含有特定的方法
# 注意对于Subject实例来说, 描述符是一个'类'级别对象,只是通过实例来访问
# 所以实现如果要想得到类似于实例属性的效果,要利用传入的instance参数来查表区分不同instance的自己的东西
class Descriptor:
    def __get__(self, instance, owner):
        print('[GET]:')
        print(self, instance, owner, sep="\n")

    def __set__(self, instance, value):
        print('[SET:')
        print(self, instance, value, sep="\n")


class Subject:
    attr = Descriptor()  # 将对attr访问定向到描述符类的一个实例
# 这里所有的Subject实例共享一个attr, 类似于单件模式.
# 除非在上面的get/set中用instance (即Subject的实例地址)去查表获取自己的copy.


class Person:
    # 更好的是将描述符类包装在使用的类上 (如果只有它用)
    class Name:  # a descriptor
        "name descriptor doc"
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name

        def __set__(self, instance, value):
            print('change...')
            instance._name = value

        def __delete__(self, instance):
            print('remove...')
            del instance._name

    name = Name()  # 连上描述符

    def __init__(self, name):
        self._name = name


class DescSquare:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value ** 2

    def __set__(self, instance, value):
        self.value = value


class Client1:
    X = DescSquare(3)


class Client2:
    X = DescSquare(32)

if __name__ == '__main__':
    x = Subject()
    a = x.attr  # -> Descriptor.__get__(Subject.attr, x, Subject)
    print()
    x.attr = 10
    print()

    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    del bob.name

    print('-'*20)
    sue = Person('Sue Jones')
    print(sue.name)

    print('-'*20)
    print(Person.Name.__doc__)
    print()

    print('-'*20)
    c1 = Client1()
    c2 = Client2()
    print(c1.X)
    c1.X = 4
    print(c1.X)
    print(c2.X)