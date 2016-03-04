import lxml.etree as ET

xml_file = 'D:/Repo/pyhod/ipxact/busdef/amba.com/AMBA4/ACE/r0p0_0/ACE_rtl.xml'

validation_path = 'http://www.spiritconsortium.org/xmlschema/spirit/1-4'

try:
    tree = ET.parse(xml_file)
    print("Good XML")
except Exception as e:
    print("Bad XML :", e)

root = tree.getroot()
print(root.tag)
print(root.attrib)
print(root.text)