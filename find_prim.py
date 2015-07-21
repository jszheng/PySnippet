__author__ = 'jszheng'
import math


def find_prims(max):
    prims = [2]
    for n in range(3, max, 2):
        is_prime = True
        for f in prims:
            if n % f == 0:
                is_prime = False
                break
        if is_prime:
            prims.append(n)
    return prims


def next_prim():
    prims = [2]
    yield 2
    n = 3
    while True:
        is_prime = True
        for f in prims:
            if n % f == 0:
                is_prime = False
                break
        if is_prime:
            prims.append(n)
            yield n
        n += 2


def is_prim(n, prims):
    if n < 2:
        return False
    s = int(math.sqrt(n)) + 1



if __name__ == '__main__':
    #max = int(input('Please input a number : '))
    #prims = find_prims(max)
    #print(prims)
    gen = next_prim()
    for i in range(1000):
        print(gen.next())
