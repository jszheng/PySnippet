import urllib.request
from bs4 import BeautifulSoup
import re
import optparse
import os

parser = optparse.OptionParser()
parser.add_option('-r', '--regexp',
                  dest="regexp",
                  action='append',
                  help='filter with regular expression',
                  )
parser.add_option('-e', '--exclude',
                  dest="exclude",
                  action='append',
                  help='exclude link regular expression',
                  )
parser.add_option('-v', '--verbose',
                  dest="verbose",
                  default=False,
                  action="store_true",
                  help='show verbose message'
                  )
parser.add_option('--version',
                  dest="version",
                  default=1.0,
                  type="float",
                  help='set program version'
                  )

options, remainder = parser.parse_args()

if options.regexp is None:
    options.regexp = []
if options.exclude is None:
    options.exclude = []

# print('VERSION : ', options.version)
# print('VERBOSE : ', options.verbose)
# print('REST    : ', remainder)

r_http_start = re.compile(r'^http://')
ignore_link = []
for url in remainder:
    print("process ", url, "......")
    root = os.path.dirname(url)
    with urllib.request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        soup = BeautifulSoup(data, 'lxml')
        # print(soup.prettify())
        for a in soup.find_all('a'):
            link = a['href']

            # include filter
            flag = False
            for filter in options.regexp:
                if re.search(filter, link):
                    flag = True
                    break
            if not flag: # no match, exclude
                ignore_link.append(link)
                continue

            # exclude filter
            flag = False
            for filter in options.exclude:
                if re.search(filter, link):
                    flag = True
                    break
            if flag: # match one exclude pattern
                ignore_link.append(link)
                continue

            # Ignore passed filtering
            # replace local link to global
            if r_http_start.search(link):
                print(link)
            else:
                print(os.path.join(root, link))

    print('Exclude these links:')
    for l in ignore_link:
        if r_http_start.search(l):
            print(l)
        else:
            print(os.path.join(root, l))
    print('Done!\n')