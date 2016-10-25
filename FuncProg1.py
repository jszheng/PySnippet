import math


def until(n, filter_func, v):
    if v == n: return []
    if filter_func(v):
        return [v] + until(n, filter_func, v + 1)
    else:
        return until(n, filter_func, v + 1)


def repeat(f, a):  # generator, lazy
    yield a
    for v in repeat(f, f(a)):
        yield v


def within(e, iterable):
    def head_tail(e, a, iterable):
        b = next(iterable)
        if abs(a - b) <= e: return b
        return (head_tail(e, b, iterable))

    return head_tail(e, next(iterable), iterable)


def next_(n, x):
    return (x + n / x) / 2


def sqrt(a0, e, n):
    return within(e, repeat(lambda x: next_(n, x), a0))


def numbers():
    for i in range(1024):
        print("=", i)
        yield i


def sum_to(n):
    sum = 0
    for i in numbers():
        if i == n: break
        sum += i
    return sum


def isprimer(n):
    def isprime(k, coprime):
        """Is k relatively prime to the value coprime?"""
        if k < coprime * coprime: return True
        if k % coprime == 0: return False
        return isprime(k, coprime + 2)

    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return isprime(n, 3)


def isprime(p):
    if p < 2: return False
    if p == 2: return True
    if p % 2 == 0: return False
    return not any(p == 0 for p in range(3, int(math.sqrt(n)) + 1, 2))


def pfactorsl(x):
    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from pfactorsl(x // 2)
        return
    for i in range(3, int(math.sqrt(x) + 0.5) + 1, 2):
        if x % i == 0:
            yield i
            if x // i > 1:
                yield from pfactorsl(x // i)
            return
    yield x


def pfactorsr(x):
    def factor_n(x, n):
        if n * n > x:
            yield x
            return
        if x % n == 0:
            yield n
            if x // n > 1:
                yield from factor_n(x // n, n)
        else:
            yield from factor_n(x, n + 2)

    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from pfactorsr(x // 2)
        return
    yield from factor_n(x, 3)


def group_by_seq(n, sequence):
    flat_iter = iter(sequence)
    full_sized_items = list(tuple(next(flat_iter)
                                  for i in range(n))
                            for row in range(len(sequence) // n))
    trailer = tuple(flat_iter)
    if trailer:
        return full_sized_items + [trailer]
    else:
        return full_sized_items


def group_by_iter(n, iterable):
    row = tuple(next(iterable) for i in range(n))
    while row:
        yield row
        row = tuple(next(iterable) for i in range(n))


def digits(x, b):
    if x == 0: return
    yield x % b
    for d in to_base(x // b, b):
        yield d


def to_base(x, b):
    return reversed(tuple(digits(x, b)))


if __name__ == '__main__':
    mult_3_5 = lambda x: x % 3 == 0 or x % 5 == 0
    print(until(10, mult_3_5, 0))
    print(sum(n for n in range(1, 10) if n % 3 == 0 or n % 5 == 0))
    print(sqrt(3, 0.00001, 2))
    print(sum_to(5))
    print(isprimer(1789337))
    print(list(pfactorsl(1789337)))
    print(isprimer(3461))

    a = [('2', '3', '5', '7', '11'), ('13', '17', '19', '23', '29'),
         ('31', '37', '41', '43', '47'), ('53', '59', '61', '67', '71'),
         ('73', '79', '83', '89', '97'), ('101', '103', '107', '109', '113'),
         ('127', '131', '137', '139', '149'), ('151', '157', '163', '167', '173'),
         ('179', '181', '191', '193', '197'), ('199', '211', '223', '227', '229')]

    # flattern
    b = [x for line in a for x in line]
    print(b)

    # structure
    b_iter = iter(b)
    c = list(tuple(next(b_iter) for i in range(5)) for row in range(len(b) // 5))
    print(c)
    print(group_by_seq(6, b))
    for item in group_by_iter(7, b_iter):
        print(item)
    print(list(zip(b[0::2], b[1::2])))

    # with zip very simple
    print(list(zip(*(b[i::4] for i in range(4)))))
    from itertools import zip_longest

    print(list(zip_longest(*(b[i::4] for i in range(4)))))

    print(list(to_base(7, 2)))