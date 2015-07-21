def foo():
    print("Love Python, Love FreeDome")
    print("E文标点,.0123456789,中文标点,. ")
    print(locals())


class A:
    def __init__(self):
        #self._types_table = None
        pass

    def show(self):
        self.data = 1
        print(locals())

    @property
    def types_table(self):
        try:
            return self._types_table
        except AttributeError:
            self._types_table = []
            return self._types_table



if __name__ == '__main__':
    foo()

    print(globals())

    a = A()
    a.show()
    tb = a.types_table
    print(tb)
    print(type(tb))
    tb.append(1)
    a.types_table.append(2)
    print(a.types_table)