"""
test dynamic attribute and method
"""


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, attr):
        return Chain('%s/%s' % (self._path, attr))


print(Chain().schools.status.users)
print(Chain().schools.users(10).report)