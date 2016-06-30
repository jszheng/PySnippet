from collections import defaultdict

tree = lambda : defaultdict(tree)

some_dict = tree()
some_dict['colours']['favirte'] = 'Yellow'
some_dict['interfaces']['aaa']['dir'] = 'input'
some_dict['interfaces']['aaa']['wid'] = 10
some_dict['aaa']['attr'] = 'good'

import json
print(json.dumps(some_dict))