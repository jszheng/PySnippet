#!/usr/bin/python
# -*- coding: utf-8 -*-
import test_mmap
from jsonmmap import ObjectMmap
import random


def main():
    mm = ObjectMmap(-1, 1024*1024, access=test_mmap.ACCESS_WRITE, tagname='share_mmap')
    while True:
        length = random.randint(1, 100)
        p = range(length)
        mm.jsonwrite(p)
        print('*' * 30)
        print(mm.jsonread_master())

if __name__ == '__main__':
    main()