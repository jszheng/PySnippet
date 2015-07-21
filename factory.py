from classtools import ListInstance

if __name__ == '__main__':
    def factory(aClass, *args):
        return aClass(*args)

    class Spam(ListInstance):
        def doit(self, message):
            print(message)

    class Person(ListInstance):
        def __init__(self,name, job):
            self.name = name
            self.job  = job

    object1 = factory(Spam)
    object2 = factory(Person, 'Guido', 'guru')
    print(object1)
    print(object2)