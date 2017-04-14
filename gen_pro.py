import os
import re
from pathlib import Path, PurePath

header = """
TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

"""
print(header)
print()

headers = []
sources = []
include_path = set()

for path, dirs, files in os.walk('.'):
    if '.git' in dirs:
        dirs.remove('.git')

    for afile in files:
        if afile.endswith('.c') or afile.endswith('.cpp') or afile.endswith('.cc'):
            rel_path = os.path.join(path, afile)
            #rel_path = rel_path.replace('\\', '/', 1000)
            sources.append(rel_path)
            continue

        if afile.endswith('.h') or afile.endswith('.hpp'):
            rel_path = os.path.join(path, afile)
            #rel_path = rel_path.replace('\\', '/', 1000)
            headers.append(rel_path)

            p = Path(path)
            segments = p.parts
            path_seg = []
            for segment in segments:
                path_seg.append(segment)
                if segment == 'include':  # this is an include path, stop here.
                    break
            include_path.add(os.path.join(*path_seg))
            continue

print('INCLUDEPATH +=', ' \\\n'.join(sorted(include_path)))
print()

print('HEADERS +=', '\\\n'.join(headers))
print()

print('SOURCES +=', '\\\n'.join(sources))
print()
