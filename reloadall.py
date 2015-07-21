# -*- coding:utf-8 -*-

"""
reload_all.py: transitively reload nested modules
"""

import types
from importlib import reload


def status(module):
    "print out message"
    print('reloading '+module.__name__)


def transitive_reload(module, visited):
    """
    recursively load module's sub-module
    :param module: currently loaded module
    :param visited: an array of loaded module
    :return: No return
    """
    if not module in visited:
        status(module)
        reload(module)
        visited[module] = None
        for attrobj in module.__dict__.values():
            if type(attrobj) is types.ModuleType:
                transitive_reload(attrobj, visited)


def reload_all(*args):
    "entry of reload function"
    visited = {}
    for arg in args:
        if type(arg) is types.ModuleType:
            transitive_reload(arg, visited)
        else:
            print("Not a Module: ", arg)

if __name__ == '__main__':
    import reloadall
    from reloadall import reload_all
    import os
    import tkinter

    print('reload_all(os)')
    reload_all(os)
    print()
    print('reload_all(tkinter)')
    reload_all(tkinter)

    help(reloadall)