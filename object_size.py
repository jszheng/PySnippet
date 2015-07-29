__author__ = 'jszheng'
import sys
from collections import namedtuple


class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

if __name__ == '__main__':
    slot1 = Date(1942, 3, 12)
    print("Slot Size", sys.getsizeof(slot1))

    NTDate = namedtuple('NTDate', ['year', 'month', 'day'])
    nt1 = NTDate(1942, 3, 12)
    print("Nametuple Size", sys.getsizeof(nt1))

    Hash = {'year': 1942, 'month':3, 'day':12}
    print("Hash Size", sys.getsizeof(Hash))

    print(type(nt1))
    print(nt1.year)
    print(nt1.month)

    print(isinstance(nt1, tuple))
    print(NTDate.__bases__)
    print(dir(nt1))