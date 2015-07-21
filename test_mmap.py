__author__ = 'jszheng'

import os
import mmap

import contextlib


def test_mmap_file():
    bigfile = 'D:/work2/code/gfx9-gen/out/textri-greenland-tee.log'
    size = os.path.getsize(bigfile)
    print("file size is ", size)
    with open(bigfile, 'rb') as fp:
        with contextlib.closing(
                mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ)
        ) as mm:
            print(len(mm))
            line_num = 0
            line = mm.readline()
            while line:
                # process line
                # fetch next line
                line_num += 1
                line = mm.readline()
            print('total', line_num, 'lines')

# mmap call can have
#    offset=n*4096

if __name__ == '__main__':
    import timeit
    print(timeit.timeit('test_mmap_file()', setup='from __main__ import test_mmap_file', number=1))

    import cProfile
    import pstats
    pr = cProfile.Profile()
    pr.snapshot_stats()
    pr.enable()
    # do somethong
    test_mmap_file()
    # end of something
    pr.disable()
    pr.print_stats()
    pr.dump_stats('test_mmap_profile.log')


