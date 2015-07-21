"""
File classtools.py(new)
Assorted class Utilities and tools
"""


class AttrDisplay:
    """
    Provides an inheritable print overload method that displays
    instances with their class names and name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """
    def __gather_attrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.__gather_attrs())


class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of
    instance via inheritance of __str__, coded here; displays
    instance attrs only; self is the instance of lowest class;
    use __X names ot avoid clashing with clients attrs
    """
    def __str__(self):
        return 'Instance of %s. address %s:\n<\n%s>' % (
            self.__class__.__name__,
            id(self),
            self.__attrnames()
        )

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result


class ListInherited:
    """
    Use dir() to collect both instance attrs and names
    inherited from its classes; Python 3.0 shows more
    names than 2.6 because of the implies object superclass
    in the new-style class model; getattr() fetches inherited
    names not in self.__dict__; use __str__, not __repr__
    or else this loops when printing bound methods!
    """
    def __str__(self):
        return 'Instance of %s. address %s:\n<\n%s>' % (
            self.__class__.__name__,
            id(self),
            self.__attrnames()
        )

    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__': # skip internals
                result += '\tname %s=<>\n' % attr
            else:
                result += '\tname %s=%s\n' % (attr, getattr(self, attr))
        return result


class ListTree:
    """
    Mix-in that returns an __str__ trace of the entire class
    tree and all its objects' attrs at and above self;
    run by print(), str() returns constructed string;
    use __X attr names to avoid impacting clients;
    use generator expr to recurse to superclasses;
    user str.format() to make substitutions clearer
    """
    def __str__(self):
        self.__visited = {}
        return 'Instance of {0}. address {1}:\n<\n{2}{3}>'.format(
            self.__class__.__name__,
            id(self),
            self.__attrnames(self, 0),
            self.__listclass(self.__class__, 4)
        )

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}: address {2}: (see above)>\n'.format(
                dots,
                aClass.__name__,
                id(aClass)
            )
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c, indent+4) for c in aClass.__bases__)
            return '\n{0}<Class {1}: address {2}:\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                self.__attrnames(aClass, indent),
                ''.join(genabove),
                dots
            )

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent+4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):  # skip internals
                result += spaces + 'name {0}=<>\n'.format(attr)
            else:
                result += spaces + 'name {0}={1}\n'.format(attr, getattr(self, attr))
        return result

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)

    class Spam(ListInstance):
        def __init__(self):
            self.data = 'food'

    x = Spam()
    print(x)

    class Parent:
        def __init__(self):
            self.data1 = 'spam'

        def ham(self):
            pass

    class Child(Parent, ListTree):
        def __init__(self):
            super().__init__()
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self):
            pass

    x = Child()
    print(x)

    from tkinter import Button

    class MyButton(ListTree, Button):
        pass

    B = MyButton(text='spam')
    open('savetree.txt', 'w').write(str(B))
