__author__ = 'jszheng'


"""
class myint:
    def __init__(self): pass
    def each:
        for i in data
            yield i

this is a test file
on iterator
"""


# 产生器, yield! 保留当前状态, 下次call时候继续
# 节省空间,lazy eval
def gen_square(N):
    for m in range(N):
        yield m ** 2


if __name__ == '__main__':
    # 构造一个list, 简单的for
    alist = [x ** 2 for x in range(10)]
    print(alist)

    # 多个循环嵌套
    b_list = [x + y
              for x in [0, 1, 2]
              for y in [100, 200, 300]]
    print(b_list)

    # 循环加上过滤器
    c_list = [x for x in range(10) if x % 2 == 0]
    print(c_list)

    # 测试gen
    for i in gen_square(5):
        print(i, end=' : ')
    print('')

    # gen转为list
    g = list(gen_square(6))
    print(g)

    # zip构造dict
    keys = ['a', 'b', 'c']
    vals = [3, 5, 8]
    z = dict(zip(keys, vals))
    print(z)

    # 数字转整数字符串
    print(bin(10))
    print(type(bin(10)))
    print(oct(10))
    print(hex(255))
    # 字串转整数
    print(int('0b1010', 2))
    print(int('0o12', 8))
    print(int('0xff', 16))
    print(float('1e-003'))

    s = {'s', 'p', 'a', 'm'}
    print(type(s))
    s.add('slot')
    print(s)