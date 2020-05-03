class MyClass:
    def __init__(self):
        pass

    __import__('subs')


m = MyClass()
print(dir(m))
m.foo()