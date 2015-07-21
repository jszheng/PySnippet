__author__ = 'jszheng'

sample_test = '''
    this is a test
    this is a test
     this is a test
    a lot lot of of of of of of of of ofo fof ofofo foofof
    text text text text text text text text text text
    '''

import textwrap

print(textwrap.fill(sample_test, width=50))

dedent_text = textwrap.dedent(sample_test)
print(dedent_text)

dedent_text = dedent_text.strip()
for width in [45, 70]:
    print('%d columns: \n' % width)
    print(textwrap.fill(dedent_text, width=width))
    print()
