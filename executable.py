# 单行语句字符串
exec("print('pythoner.com')")

#  多行语句字符串
exec("""
for i in range(5):
    print("iter time: %d" % i)
""")


x = 7
eval('print(3*x)')

my_source_code = '''
def foo(a, b):
    return a+b
'''

print("Compile source code")
my_executable = compile(my_source_code, '', 'exec')
print(type(my_executable))
#exec(my_executable)


import pickle

print("Save in Pickle")
with open('code.pickle', 'wb') as dbfp:
    pickle.dump(my_executable, dbfp)

print("Load back Pickle")
with open('code.pickle', 'rb') as dbfp:
    my_code = pickle.load(dbfp)
print("execute code")
exec(my_code)
print("Now use the new code")
print(foo(2,4))
