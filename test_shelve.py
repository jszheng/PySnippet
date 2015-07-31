# python shelve

#Author : Hongten
#MailTo : hongtenzone@foxmail.com
#QQ     : 648719819
#Blog   : http://www.cnblogs.com/hongten
#Create : 2013-08-09
#Version: 1.0

import shelve

'''
    python中的shelve模块，可以提供一些简单的数据操作
    他和python中的dbm很相似。

    区别如下：
    都是以键值对的形式保存数据，不过在shelve模块中，
    key必须为字符串，而值可以是python所支持的数据
    类型。在dbm模块中，键值对都必须为字符串类型。

    sh['a'] = 'a'
    sh['c'] = [11, 234, 'a']
    sh['t'] = ('1', '2', '3')
    sh['d'] = {'a':'2', 'name':'Hongte' }
    sh['b'] = 'b'
    sh['i'] = 23

    我们可以获取一个shelve对象
    sh = shelve.open('c:\\test\\hongten.dat', 'c')

    删除shelve对象中的某个键值对
    del sh['d']

    遍历所有数据
    for item in sh.items():
        print('键[{}] = 值[{}]'.format(item[0], sh[item[0]]))

    获取某个键值对
    print(sh['a'])

    关闭shelve对象:
    sh.close()

    ####################################################
    ####        API中强调
    Do not rely on the shelf being closed automatically;
    always call close() explicitly when you don’t need
    it any more, or use a with statement with
    contextlib.closing().
    ####################################################

'''
#global var
#是否显示日志信息
SHOW_LOG = True


def get_shelve():
    '''open -- file may get suffix added by low-level library'''
    return shelve.open('hongten', 'c')


def save(sh):
    '''保存数据'''
    if sh is not None:
        sh['name'] = 'Hongten'
        sh['gender'] = 'M'
        sh['address'] = {'hometown': 'Shuifu,Yunnan', 'nowadd': 'Guangzhou,Guangdong'}
        sh['phone'] = ('13423****62', '18998****62')
        sh['age'] = 22
        if SHOW_LOG:
            for item in sh.items():
                print('保存数据[{}] = [{}]'.format(item[0], sh[item[0]]))
        sh.close()
    else:
        print('the shelve object is None!')


def update(sh):
    '''更新数据'''
    if sh is not None:
        sh['name'] = 'Hongten'
        sh['hoby'] = ('篮球', '羽毛球', '乒乓球', '游泳')
        sh['phone'] = ('13423****62', '18998****62', '020-90909090')
        sh['age'] = 23
        if SHOW_LOG:
            keys = ('name', 'hoby', 'phone', 'age')
            for item in keys:
                print('更新数据[{}] = [{}]'.format(item, sh[item]))
        sh.close()
    else:
        print('the shelve object is None!')


def delete(sh, key):
    '''删除某个数据'''
    if sh is not None:
        if SHOW_LOG:
            print('删除[{}]的数据'.format(key))
        del sh[key]
        sh.close()
    else:
        print('the shelve object is None!')


def deleteall(sh):
    '''删除所有数据'''
    if sh is not None:
        for item in sh.items():
            if SHOW_LOG:
                print('删除数据[{}] = [{}]'.format(item[0], sh[item[0]]))
            del sh[item[0]]
        sh.close()
    else:
        print('the shelve object is None!')


def fetchone(sh, key):
    '''获取某个数据'''
    if sh is not None:
        print('获取[{}]的值：{}'.format(key, sh[key]))
        sh.close()
    else:
        print('the shelve object is None!')


def fetchall(sh):
    '''遍历所有数据'''
    if sh is not None:
        for item in sh.items():
            print('数据[{}] = [{}]'.format(item[0], sh[item[0]]))
        sh.close()
    else:
        print('the shelve object is None!')


###############################################################
###                测试           START
###############################################################
def save_test():
    '''保存数据...'''
    print('保存数据...')
    sh = get_shelve()
    save(sh)


def fetchall_test():
    '''遍历所有数据'''
    print('遍历所有数据...')
    sh = get_shelve()
    fetchall(sh)


def fetchone_test():
    '''获取某个数据'''
    print('获取某个数据...')
    sh = get_shelve()
    key = 'address'
    fetchone(sh, key)


def delete_test():
    '''删除某个数据'''
    print('删除某个数据...')
    sh = get_shelve()
    key = 'hoby'
    delete(sh, key)


def update_test():
    '''更新数据...'''
    print('更新数据...')
    sh = get_shelve()
    update(sh)


def deleteall_test():
    '''删除所有数据'''
    print('删除所有数据...')
    sh = get_shelve()
    deleteall(sh)


###############################################################
###                测试           END
###############################################################

def init():
    global SHOW_LOG
    SHOW_LOG = True
    print('SHOW_LOG : {}'.format(SHOW_LOG))
    deleteall_test()
    save_test()


def main():
    init()
    print('#' * 50)
    fetchall_test()
    print('#' * 50)
    update_test()
    print('#' * 50)
    fetchall_test()
    print('#' * 50)
    fetchone_test()
    print('#' * 50)
    delete_test()
    print('#' * 50)
    fetchall_test()
    print('#' * 50)
    deleteall_test()
    print('#' * 50)
    fetchall_test()


if __name__ == '__main__':
    main()
