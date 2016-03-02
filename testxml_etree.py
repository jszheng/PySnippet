from xml.etree import ElementTree
import re

# each valid bus defintion has two xml file, 1st contains description and summary of paramter.
# 2nd has port definition (
#xmlfile = 'D:/Repo/pyhod/ipxact/busdef/amba.com/AMBA4/ACE/r0p0_0/ACE.xml'
xmlfile = 'D:/Repo/pyhod/ipxact/busdef/amba.com/AMBA4/ACE/r0p0_0/ACE_rtl.xml'

xmlns_spirit = '{http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4}'
xmlns_xsi = '{http://www.w3.org/2001/XMLSchema-instance}'
xmlns_arm = '{http://www.arm.com/SPIRIT}'


def walk(node, depth, node_actor):
    node_actor(node, depth)
    for child in node:
        walk(child, depth + 1, node_actor)


def action(node, depth):  # get rid of the spirit prefix
    prefix = re.compile(r'{.*}')
    node.tag = prefix.sub('', node.tag)
    for key, value in node.attrib.items():
        if prefix.search(key):
            newkey = prefix.sub('', key)
            node.attrib[newkey] = value
            del node.attrib[key]
            key = newkey
        if prefix.search(value):
            node.attrib[key] = prefix.sub('', value)
    if re.match(r'\s+', str(node.text)):
        node.text = ''
    print(' ' * depth * 4, node.tag, node.attrib, node.text)


def busdef_walker(node, depth, pre_actor=None, post_actor=None):
    if pre_actor:
        pre_actor(node, depth)
    for child in node:
        busdef_walker(child, depth + 1, pre_actor, post_actor)
    if post_actor:
        post_actor(node, depth)


def busdef_actor(node, depth):
    def no_action():
        pass

    def show():
        print(node.tag, ':', node.text)

    action_table = {
        'busDefinition': no_action,
        'vedor': show,
        'systemGroupNames': no_action,
        'vendorExtensions': no_action,
        'parameterNames': no_action
    }
    if node.tag in action_table.keys():
        actor = action_table[node.tag]
        actor()
    else:
        show()


def busdef_post_actor(node, depth):
    pass


class IPXACT_busdef:
    def __init__(self):
        self.attribute = {}
        self.name_array = []
        pass

    def no_action(self): # shared between pre and post actor
            pass

    def pre_actor(self, node, depth):
        def default_action():
            self.attribute[node.tag] = node.text

        def start_accumulate():
            self.name_array = []

        def add_name():
            self.name_array.append(node.text)

        action_table = {
            'busDefinition': self.no_action,
            'vendorExtensions': self.no_action,
            'systemGroupNames': start_accumulate,
            'parameterNames': start_accumulate,
            'systemGroupName': add_name,
            'parameterName': add_name,
        }
        if node.tag in action_table.keys():
            actor = action_table[node.tag]
            actor()
        else:
            default_action()

    def post_actor(self, node, depth):
        def add_system_group_names():
            self.attribute['systemGroupNames'] = self.name_array
        def add_parameter_names():
            self.attribute['parameterNames'] = self.name_array
        action_table = {
            'systemGroupNames': add_system_group_names,
            'parameterNames': add_parameter_names
        }
        if node.tag in action_table.keys():
            actor = action_table[node.tag]
            actor()

    def walk(self, node, depth=0):
        self.pre_actor(node, depth)
        for child in node:
            self.walk(child, depth + 1)
        self.post_actor(node, depth)


with open(xmlfile, 'rt') as f:
    tree = ElementTree.parse(f)
    print(tree)

    # for node in tree.iter():
    #    print(node.tag)

    root = tree.getroot()
    # print(root.tag)
    # print(root.attrib)
    # for child in root:
    #     print(child.tag, child.attrib)
    walk(root, 0, action)
    tree.write('output.xml')

    print("################################################")
    print("############    understanding...   #############")
    print("################################################")
    # if root.tag == 'busDefinition':
    #     busdef_walker(root, 0, busdef_actor)

    # process summary xml
    # busdef = IPXACT_busdef()
    # busdef.walk(root)
    # for key, value in busdef.attribute.items():
    #     print(key, ':', value)

    # process rtl xml
    for port in tree.iter('port'):
        name = port.find('logicalName').text
        description = port.find('description').text
        direction = port.find('wire/onMaster/direction').text

        width_node = port.find('wire/onMaster/width')
        if width_node is not None:
            width = width_node.text
        else:
            width = '#'


        print(name, direction, width, description)

    for param in tree.iter('parameters'):
        