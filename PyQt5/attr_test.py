class MyTest:
    class_var = 10

    def __init__(self):
        pass


t = MyTest()
print("before Init")
print(MyTest.class_var)
print(t.class_var)
t.class_var = 20
print("assign inst")
print(MyTest.class_var)
print(t.class_var)
