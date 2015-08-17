
import textwrap

sample_text = """
This is a textwrap module can be used to format text from output in situation where pretty-printting is desi
. it offers programmati functionality similuar to the paragraph wrapping of fillin g features found in
many text editors

1. item 1
2. item 2
3. item 3
"""

print('No Dedent:')
print(textwrap.fill(sample_text, width=50))

