__author__ = 'jszheng'

print('demo iterator')
datas = [1, 2, 3, 4]
i = iter(datas)

print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
#print(i.__next__())

print('demo generator')
def numbers(ary):
    for item in ary:
        yield '%d' % item

g = numbers(datas)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

print('used in for')
g = numbers(datas)
for x in g:
    print(x)

print('test generator expression')
def square(x):
    return x*x

genexp =(square(x) for x in range(6))
for s in genexp:
    print(s)
