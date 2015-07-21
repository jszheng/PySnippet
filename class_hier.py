from platform import python_version

class Base:
    def __init__(self):
        self.base_data = 1

    def incr(self):
        self.base_data += 1

    def __str__(self):
        return self.base_data.__str__()


class Derive(Base):
    def __init__(self):
        super().__init__()
        self.derive_data = 10.0

    def incr(self):
        super.incr()
        self.derive_data += 1.0

    def __str__(self):
        return super().__str__()+','+self.derive_data.__str__()


def pobj(a: object):
    print(a)

if __name__ == '__main__':
    a = Base()
    print(a)
    a.incr()
    print(a)
    pobj(a)

    b = Derive()
    print(b)
    pobj(b)

    print(isinstance(None, object))
    print(type(None) == object)
    print(None is object)
    num = 1/3
    print(repr(num))
    print(str(1/3))
    print(1/3)

    print('Python', python_version())
    st = 'strings are now '
    print(st, type(st))
    bs = b'byte array'
    print(bs, type(bs))
    ba = bytearray(bs)
    print(ba, type(ba))

