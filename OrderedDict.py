__author__ = 'jszheng'

from collections import OrderedDict


if __name__ == '__main__':
    # dict
    d = {}
    d['banana'] = 3
    d['apple'] = 4
    d['pear'] = 2
    d['organe'] = 1

    od = OrderedDict()
    od['banana'] = 3
    od['apple'] = 4
    od['pear'] = 2
    od['organe'] = 1

    # print('Normal Dict')
    # for (k, v) in d.items():
    #     print(k, '=', v)
    #
    # print('Ordered Dict')
    # for (k, v) in od.items():
    #     print(k, '=', v)

    print(d)
    print(od)
    sod_key = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
    print(sod_key)
    sod_val = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    print(sod_val)
    print(list(od.keys()))
