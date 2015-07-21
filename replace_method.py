# coding=utf-8
"""
this is a test of replace method
"""


class A(object):
    def b(self):
        print('ok')


a = A()
print(A.b, a.b)

var = A.__dict__['b']
print(var, A.b)
a.b()

def c(self):
    print('not ok')


A.b = c  # 换函数了

print(A.b, a.b)
print(A.__dict__['b'], A.b)

a.b()

print(getattr(a, 'b'))