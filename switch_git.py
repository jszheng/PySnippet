#!python3

import os
import sys
import re
import shutil

path_done = set()


def find_n_replace(git_path):
    config_path = os.path.join(git_path, ".git/config")
    subm_path = os.path.join(git_path, ".gitmodules")

    with open(config_path, 'rt') as f:
        of = open('config_new', 'wt')
        for line in f:
            if re.search(r'url\s*=(.*)192\.168\.100\.10', line):
                print(line, end='')
                newline = re.sub(r'192\.168\.100\.10', r'git.iluvatar.ai', line)
                print(newline, end='')
                of.write(newline)
            else:
                of.write(line)
    of.close()
    shutil.move('config_new', config_path)

    if os.path.exists(subm_path) and os.path.isfile(subm_path) :
        changed = False
        with open(subm_path, 'rt') as f:
            of = open('gitsubmodule_new', 'wt')
            for line in f:
                if re.search(r'url\s*=(.*)192\.168\.100\.10', line):
                    print(line, end='')
                    newline = re.sub(r'192\.168\.100\.10', r'git.iluvatar.ai', line)
                    print(newline, end='')
                    of.write(newline)
                    changed = True
                else:
                    of.write(line)
        of.close()
        if changed:
            shutil.move('gitsubmodule_new', subm_path)
            print('    [!] Please commit your .gitmodules file')


# copy from os.walk
def walk(top, onerror=None, followlinks=False):
    dirs = []
    nondirs = []

    try:
        scandir_it = os.scandir(top)
        entries = list(scandir_it)
    except OSError as error:
        if onerror is not None:
            onerror(error)
        return

    for entry in entries:
        try:
            is_dir = entry.is_dir()
        except OSError:
            is_dir = False

        if is_dir:
            dirs.append(entry.name)
        else:
            nondirs.append(entry.name)

    ############################################
    # yield top, dirs, nondirs
    if '.git' in dirs:
        git_path = os.path.abspath(top)
        path_done.add(git_path)
        print("[GIT]", top)
        find_n_replace(git_path)
        return
    else:
        pass
        #print("[PASS]", top)
    ############################################

    # Recurse into sub-directories
    islink, join = os.path.islink, os.path.join
    for dirname in dirs:
        new_path = join(top, dirname)
        if followlinks or not islink(new_path):
            walk(new_path, onerror, followlinks)


if __name__ == '__main__':
    # deal with command line path
    if len(sys.argv) > 1:
        paths = sys.argv[1:]
        script_path = sys.argv[0]
    else:  # or use current directory as default
        paths = ['.']

    # iterate each top
    for p in paths:
        walk(p)