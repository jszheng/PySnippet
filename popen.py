import subprocess

"""
pingP = subprocess.Popen(args='ping -n 4 www.sina.com.cn', shell=True, stdout=subprocess.PIPE)
pingP.wait()
print(pingP.stdout.read())
print(pingP.pid)
print(pingP.returncode)
"""
# linux
#pingP = subprocess.Popen(args='cat', shell=True, stdin=subprocess.PIPE)
#pingPout, pingPerr = pingP.communicate(input='Hello Python')
#print(pingPout.read())

try:
    returncode = subprocess.call('dir', shell=True)
    if returncode < 0:
        print('Child process was terminated by signal', returncode)
    else:
        print('Child process returned with code ', returncode)
except(OSError, e):
    print("Execution Failed! :　")




