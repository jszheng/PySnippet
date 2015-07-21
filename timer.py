__author__ = 'jszheng'
"""
timer.py: a decorator to measure function execution time
"""
import time

def timer(label='', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.clock()
            result = self.func(*args, **kwargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                format_str = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format_str % values)
            return result
    return Timer


if __name__ == '__main__':
    @timer(label='[CCC]==>')
    def listcomp(N):
        return [x * 2 for x in range(N)]
    # timer(label='[CCC]==>')(listcomp(N)) -> listcomp
    # Timer(listcomp(N))                   -> listcomp
    # 返回一个Timer类,用该类构造函数包裹原来的函数构造一个新的实例, 其中
    #   记录下该函数, 初始化他的总执行时间
    #   定义调用时的行为
    #      执行该函数, 记录时间
    #      需要时候打印 trace 信息
    #      返回结果

    @timer(trace=True, label='[MMM]==>')
    def mapcall(N):
        return map((lambda x: x*2), range(N))

    for func in (listcomp, mapcall):
        print('')
        result = func(5)
        func(5000)
        func(50000)
        func(100000)
        print(result)
        print('all time = %s' % func.alltime)


