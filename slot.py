__author__ = 'jszheng'


class MyClass:
    __slots__ = ['age', 'name', 'job']


class D:
    __slots__ = ['a', 'b', '__dict__']
    c = 33

    def __init__(self):
        self.d = 4

if __name__ == '__main__':
    m = MyClass
    m.age = 10
    print(m.age)
    print(dir(m))  # 没有__dict__属性

    x = D()
    print(x.__dict__)
    print(x.__slots__)
    print(x.c)
    x.a = 1
    x.b = 2
    print(getattr(x, 'a'))
    print(getattr(x, 'b'))
    print(dir(x))

    print('list all attr:')
    for attr in list(getattr(x, '__dict__', [])) + getattr(x, '__slots__', []):
        print(attr, '=>', getattr(x, attr))

