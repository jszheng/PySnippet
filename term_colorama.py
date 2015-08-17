"""
Test crosss platform terminal color
https://pypi.python.org/pypi/colorama

"""

import colorama

colorama.init()

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Fore.RESET + Back.RESET + Style.RESET_ALL)
print('back to normal now')
print('\033[31m' + 'some red text')
print('\033[30m')  # and reset to default color