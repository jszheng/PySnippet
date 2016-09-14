import os
from collections import OrderedDict


class PathNode:
    def __init__(self):
        self.parent = None
        self.path = ''
        self.sub_node = OrderedDict()
        self.attribute = []

    def add_node(self, path_ary, *args):
        if len(path_ary) == 0:
            print("Warning: path ary is empty when calling add_node from %s" % self.path)
            return

        name = path_ary.pop(0)
        attr = args

        if name in self.sub_node:
            if len(path_ary) ==0:
                print("Warning: re-define %s/%s" % (self.path, name))
                self.sub_node[name].attribute = args
            else:
                self.sub_node[name].add_node(path_ary, *args)
        else:
            node = PathNode()
            node.parent = self
            node.path = self.path + '/' + name
            if len(path_ary) != 0:
                print("Warning: %s/%s not defined but want to define %s/%s/%s" %
                      (self.path, name, self.path, name, ('/').join(path_ary)))
                node.add_node(path_ary, *args)
            else:
                node.attribute = attr
            self.sub_node[name] = node


class PathHash:
    def __init__(self):
        self.root_node = PathNode()

    def add_node(self, path, *args):
        path_ary = path.split('/')
        self.root_node.add_node(path_ary, *args)


if __name__ == '__main__':
    root = PathHash()
    root.add_node('a', 1, 2)
    root.add_node('a/b', 3, 4)
    root.add_node('a/c', 5, 6)
    root.add_node('a/c/d', 7, 8)
    root.add_node('e', 1, 1)
    root.add_node('e/f', 3, 5)
    root.add_node('g/h', 4, 4)
    print('done!')