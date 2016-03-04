from xml.etree.ElementTree import iterparse
import logging

#def parse_and_remove(filename, path):
def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass
        #elif event == 'start-ns':


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        self.reverse_table = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'

    def __call__(self, path):
        return path.format_map(self.namespaces)

if __name__ == '__main__':
    logging.basicConfig(
        #filename='run.log',
        level=logging.ERROR
    )
    logging.warning("Hello!")
    # ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
    # print(ns('content/{html}html'))
    # print(ns('content/{html}html/{html}head/{html}title'))
    xmlfile = 'D:/Repo/pyhod/ipxact/busdef/amba.com/AMBA4/ACE/r0p0_0/ACE_rtl.xml'
    ns = XMLNamespaces()
    it = iterparse(xmlfile, ('start', 'end', 'start-ns', 'end-ns'))
    for event, elem in it:
        #print(event, elem)
        if event == 'start-ns':
            name, value = elem

            ns.register(name, value)
        if event == 'start':
            break # do not need to go down
    print(ns.namespaces)

