import time
import sys

reps = 10000
repslist = range(reps)


# 测量时间函数
def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs, **kargs)
    e = time.clock() - start
    return e, ret


def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res


def listComp():
    return [abs(x) for x in repslist]


print(sys.version)
for test in (forLoop, listComp):
    elapsed, result = timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, elapsed, result[0], result[-1]))