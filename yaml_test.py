import yaml
import json

filename = 'D:/work2/code/gfx9-gen/out/dj_flows.yaml'
f = open('test.yaml')

x = yaml.load(f)

print(yaml.dump(x))

print('')
import pprint
pprint.pprint(x)

print('')
import json

fp = open('test.json', 'w')
json = json.dump(x, fp)
