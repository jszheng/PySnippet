__author__ = 'jszheng'

import optparse
import sys

print('ARGV : ', sys.argv[1:])

parser = optparse.OptionParser()
parser.add_option('-o', '--output',
                  dest="out_file",
                  default="default.out",
                  help='set output file name',
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

print('VERSION : ', options.version)
print('VERBOSE : ', options.verbose)
print('OUTPUT  : ', options.ofile)
print('REST    : ', remainder)
