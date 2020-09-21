import os
import optparse
import subprocess
import io
import re
import cxxfilt

def get_application(name, error_msg=''):
    p = subprocess.Popen(['which', name], stdout=subprocess.PIPE)
    out, err = p.communicate()
    file_name = out.rstrip().decode()

    # check command
    if p.returncode:
        print("Can't find", name, error_msg)
        exit(1)
    if not os.path.isfile(file_name):
        print(file_name, "is not a file!")
        exit(1)

    return file_name


def dump_and_filter(file_name, cmd):
    p = subprocess.Popen([cmd, '-t', file_name], stdout=subprocess.PIPE)
    out, err = p.communicate()

    if p.returncode:
        return file_name+" Dump Error!"

    so = ""
    pattern = re.compile(r'_Z[^\s]+')
    for line in out.decode().split('\n'):
        #print(line)
        srcs = re.findall(pattern, line)
        #print(srcs)
        new_line = line
        if len(srcs) == 0:
            so += line+"\n"
            continue
        for src in srcs:
            dst = cxxfilt.demangle(src)
            #print(dst)
            new_line = re.sub(src, dst, new_line)
            #print(new_line)
        so += new_line+"\n"
        #print()
    return so


if __name__ == '__main__':
    usage = "usage: %prog [options] bin_file [bin_file ...]"
    parser = optparse.OptionParser(usage=usage)
    # TODO ...
    options, remainder = parser.parse_args()

    # check cuda application path
    objdump = get_application('objdump')

    for file_name in remainder:
        if not os.path.isfile(file_name):
            print(file_name, "does not exist!")
            continue

        #print(file_name, objdump)
        ofname = file_name + '.sym'
        with open(ofname, 'w') as of:
            of.write(dump_and_filter(file_name, objdump))
