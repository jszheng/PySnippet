__author__ = 'jszheng'
import pprint


class Structure:
    # class variable that specifies expected fields
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # set arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x', 'y']

    class Circle(Structure):
        _fields = ['radius']

    s = Stock('ACME', 50, 91.1)
    p = Point(2, 3)
    c = Circle(4.5)

    print(dir(s))
    print(s._fields)
    print(s.name)
    print(dir(p))
    print(p._fields)
    print(dir(c))
    print(c._fields)

    # trigger error
    s2 = Stock('ACME', 50)