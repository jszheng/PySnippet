import os

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
            rel_path = rel_path.replace('\\', '/', 1000)
            sources.append(rel_path)
            continue

        if afile.endswith('.h') or afile.endswith('.hpp'):
            rel_path = os.path.join(path, afile)
            rel_path = rel_path.replace('\\', '/', 1000)
            headers.append(rel_path)
            include_path.add(os.path.dirname(rel_path))
            continue

print('INCLUDEPATH +=', '\\\n'.join(include_path))
print()

print('HEADERS +=', '\\\n'.join(headers))
print()

print('SOURCES +=', '\\\n'.join(sources))
print()
