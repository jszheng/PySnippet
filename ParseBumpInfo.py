import pandas as pd
import re

# read the data
bump_file = '/home/jszheng/Downloads/XY coordinates and pin assignment.xlsx'
df = pd.DataFrame(pd.read_excel(bump_file, sheet_name='4-2.HW PA'))
x = df['BumpX\n(Tester View)'].values.tolist()
y = df['BumpY\n(Tester View)'].values.tolist()
names = df['Bump Name'].values.tolist()

scanio = df[df['Bump Name'].str.match('^SCANIO.*')==True]
print(scanio)
vdd = df[df['Bump Name']=='VDD_CORE']
print(vdd)
exit(1)

# expand array [n] to _n style to match with tester report
name = []
name_cnt = dict()
ary_pat = re.compile(r'\[(\d+)\]')
for n in names:
    new = ary_pat.sub(r'_\1', n)
    name.append(new)
    if new in name_cnt:
        name_cnt[new] += 1
    else:
        name_cnt[new] = 1

# Find out signals that has more than 1 location
# for key, value in name_cnt.items():
#     if value > 1:
#         print(key, "\t\t\t", value)

vdd_x = []
vdd_y = []
vss_x = []
vss_y = []
scan_x = []
scan_y = []
sig_x = []
sig_y = []
other = 0
for item in zip(name, x, y):
    iname, ix, iy = item
    if iname == 'VDD_CORE':
        vdd_x.append(ix)
        vdd_y.append(iy)
    elif iname == 'VSS':
        vss_x.append(ix)
        vss_y.append(iy)
    elif iname[0:6] == 'SCANIO':
        scan_x.append(ix)
        scan_y.append(iy)
    else:
        sig_x.append(ix)
        sig_y.append(iy)
        other += 1

print('Total   ', len(x), len(y))
print('VDD     ', len(vdd_x), len(vdd_y))
print('VSS     ', len(vss_x), len(vss_y))
print('scan    ', len(scan_x), len(scan_y))
print('Signals ', other, len(sig_x), len(sig_y))

import pickle

with open('bump_info.dat', 'wb') as pkfile:
    pickle.dump([sig_x, sig_y, scan_x, scan_y, vdd_x, vdd_y, vss_x, vss_y], pkfile)
