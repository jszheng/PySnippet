__author__ = 'jszheng'

import sys

if __name__ == '__main__':
    print(sys.argv)
    print(len(sys.argv))
    if len(sys.argv) > 1:
        for file in sys.argv[1:]:
            print(file)
    else:
        # read from input
        strings = sys.stdin.read()
        print(strings)