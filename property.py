__author__ = 'jszheng'

# 在__dict__中的东西是attribute (用buildin方法 vars(obj)获取obj.__dict__) locals(), globals()
# 而property是指getter/setter方法的重载[方法属性], 其实就是描述符的另外一种表现

class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setName(self, value):
        self._name = value

    def delName(self):
        del self._name

    name = property(getName, setName, delName, 'name property doc')


# 用property方式
class deco_property:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        "name property docs"
        print('fetching...')
        return self._name

    @name.setter
    def name(self, value):
        print("change...")
        self._name = value

    @name.deleter
    def name(self):
        print('remove...')
        del self._name


# 描述符


if __name__ == '__main__':
    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    print()

    bob = deco_property('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    del bob.name

    print('-'*20)
    sue = deco_property('Sue Jones')
    print(sue.name)
    print(deco_property.name.__doc__)
    print()


