__author__ = 'jszheng'

import math
import fractions
import functools
import operator


def pollard_prim(n):
    primlist = []
    for i in range(2, n):
        while n != i:
            if (n % i) == 0:
                primlist.append(i)
                n = int(n/i)
            else:
                break
    primlist.append(n)
    return primlist


def lcm(m, n):
    gcd = fractions.gcd(m, n)
    mr = int(m/gcd)
    nr = int(n/gcd)
    return mr*nr*gcd


def common_list(l1, l2):
    r = []
    for i in l1:
        r.append(i)
        if i in l2:
            l2.remove(i)
    for i in l2:
        r.append(i)
    return r


if __name__ == '__main__':
    T1 = 11
    T2 = 17
    S1 = 0
    S2 = 3
    # 1 step, adjust start
    tmin = min(T1, T2)
    tmin_start = S1 if(tmin == T1) else S2
    tmax = max(T1, T2)
    tmax_start = S1 if(tmax == T1) else S2
    while abs(tmin_start-tmax_start) > tmax:
        if tmin_start < tmax_start:
            tmin_start += tmin
        else:
            tmax_start += tmax
    # list all possible value
    lcm = lcm(tmin, tmax)
    nmin = int(lcm/tmin)
    nmax = int(lcm/tmax)
    deltas = set()
    while (nmin >= 0) and (nmax >= 0):
        print("debug", tmin_start, tmax_start)
        if tmin_start < tmax_start:
            delta = tmax_start - tmin_start
            deltas.add(delta)
            deltas.add(tmax - delta)
            tmin_start += tmin
            nmin -= 1
        else:
            delta = tmin_start - tmax_start
            deltas.add(delta)
            deltas.add(tmax - delta)
            tmax_start += tmax
            nmax -= 1
    print("*"*50)
    print("* All Deltas")
    print("*"*50)
    print(deltas)
    # number1 = int(input('Please input a number : '))
    # pl1 = pollard_prim(number1)
    # print(pl1)
    # number2 = int(input('Please input a number : '))
    # pl2 = pollard_prim(number2)
    # print(pl2)
    # cl = common_list(pl1, pl2)
    # print(cl)
    # print(functools.reduce(operator.mul, cl))
    # print("gcd =", fractions.gcd(number1, number2))
    # print("lcm =", lcm(number1, number2))