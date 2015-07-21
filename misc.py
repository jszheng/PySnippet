__author__ = 'jszheng'

from calendar import prcal
#year = int(input("Type the year number:"))
prcal(2015)

''' test class attribute'''
class rect:
    """this is a test"""
    l = 8

    @classmethod
    def display(cls):
        print(cls.l)

    @staticmethod
    def disp_msg():
        print("Length is 50")

print(rect.__name__)
print(rect.__bases__)
print(rect.__dict__)
print(rect.__doc__)
print(rect.__module__)
i1 = rect()
i1.display()

rect.disp_msg()
i1.disp_msg()

class rect:
    n=0

    def __init__(self,x,y):
        rect.n +=1
        self.l=x
        self.b=y

    def __del__(self):
        rect.n -=1
        class_name = self.__class__.__name__
        print(class_name,' destroyed')

    def rectarea(self):
        print ('Area of rectangle is ', self.l * self.b)

    def noOfObjects(self):
        print ('Number of objects are: ', rect.n)

r=rect(3,5)
r.rectarea()
r.noOfObjects()
s=rect(5,8)
s.rectarea()
r.noOfObjects()
del r
s.noOfObjects()
del s

