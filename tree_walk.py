import os
import time
for path, dirs, files in os.walk('..'):
    print(os.path.realpath(path))
    print(dirs)
    print(files)