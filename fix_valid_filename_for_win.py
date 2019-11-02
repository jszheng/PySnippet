import os
import sys
import shutil
import glob
import re

if __name__ == '__main__':
    for file_name in glob.glob("/home/jszheng/Syncthing_share/Courses/李宏毅/*"):
        base, stem = os.path.split(file_name)
        changed = False
        new_stem = stem
        if re.search(r'\:', stem):
            new_stem = new_stem.replace(':', "")
            changed = True
        if re.search(r',', new_stem):
            new_stem = new_stem.replace(',', '')
            changed = True
        if changed:
            new_path = os.path.join(base, new_stem)
            print("mv", file_name, new_path)
            shutil.move(file_name, new_path)