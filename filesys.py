__author__ = 'jszheng'

import os
import sys
import pathlib
from pathlib import Path
import os.path
import glob
import tempfile

lorem = '''this is a very long
long long long
long long lon
test'''


def make_tempfile():
    fd, temp_file_name = tempfile.mkdtemp()
    os.close(fd)
    f = open(temp_file_name, 'wt')
    try:
        f.write(lorem)
    finally:
        f.close()
    return temp_file_name


def cleanup(filename):
    os.unlink(filename)


if __name__ == '__main__':
    print(os.name)
    # using pathlib
    print(Path.cwd())
    p1 = Path('.')
    print(p1)
    print(p1.stat())
    print(p1.resolve())
    for file in sorted(p1.glob("*.py")):
        print(file)
    # using os.path
    print(os.path.abspath('.'))
    for name in glob.glob('*.py'):
        print(name)

    with open(sys.argv[0], 'r') as file:
        for line in file:
            print(line)

    usrinput = sys.stdin.readline()
    print(usrinput)