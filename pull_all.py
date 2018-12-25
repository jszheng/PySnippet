import os
import sys

path_done = set()

# copy from os.walk
def walk(top, onerror=None, followlinks=False):

    top = os.fspath(top)
    dirs = []
    nondirs = []
    walk_dirs = []

    try:
        scandir_it = os.scandir(top)
    except OSError as error:
        if onerror is not None:
            onerror(error)
        return

    with scandir_it:
        while True:
            try:
                try:
                    entry = next(scandir_it)
                except StopIteration:
                    break
            except OSError as error:
                if onerror is not None:
                    onerror(error)
                return

            try:
                is_dir = entry.is_dir()
            except OSError:
                # If is_dir() raises an OSError, consider that the entry is not
                # a directory, same behaviour than os.path.isdir().
                is_dir = False

            if is_dir:
                dirs.append(entry.name)
            else:
                nondirs.append(entry.name)


    ############################################
    #yield top, dirs, nondirs
    if '.git' in dirs:
        path_done.add(os.path.abspath(top))
        print("[GIT]", top)
        print(os.system("pushd " + top + "; git pull; popd"))
        return
    if '.svn' in dirs:
        print("[SVN]", top)
        return
    else:
        print("[PASS]", top)
    ############################################

    # Recurse into sub-directories
    islink, join = os.path.islink, os.path.join
    for dirname in dirs:
            new_path = join(top, dirname)
            if followlinks or not islink(new_path):
                walk(new_path, onerror, followlinks)


if __name__ == '__main__':
    # deal with command line path
    if len(sys.argv) > 1 :
        paths       = sys.argv[1:]
        script_path = sys.argv[0]
    else: # or use current directory as default
        paths = ['.']

    # iterate each top
    for p in paths:
        walk(p)
