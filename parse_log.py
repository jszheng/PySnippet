import re
import os
import pandas as pd
import optparse

# file_name = '/home/jszheng/Downloads/log_0920_x0y0_new_IO.txt'
# base, ext = os.path.splitext(file_name)
# excel_fn = base+'.xlsx'

header = [
    "Number",
    "Site",
    "Test Name",
    "Pin",
    "Channel",
    "Low", " ",
    "Measured", " ",
    "Status",
    "High", " ",
    "Force", " ",
    "Loc"
]

rPassPat = re.compile(
    r'(\d+)\s+(\d+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+(\d+)')
rFailPat = re.compile(
    r'(\d+)\s+(\d+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+\((\w+)\)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+(\d+)')


# all_data = []
# def process_line(line_ary):
#     #print(line_ary)
#     all_data.append(line_ary)
#
#
# print("Parsing File", file_name, "...")
# print("These line is not parsed by this program: ")
# print("------------------------------------------------------------------")
# with open(file_name) as fp:
#     for line in fp:
#         m = rPassPat.search(line)
#         if m:
#             la = list(m.groups())
#             la.insert(9, ' ') # make it the same length, with Pass flag
#             process_line(la)
#
#             continue
#
#         m = rFailPat.search(line)
#         if m:
#             process_line(list(m.groups()))
#             continue
#
#         print(line.rstrip())
# df = pd.DataFrame(all_data, columns=header)
# print(df.head())
# writer = pd.ExcelWriter(excel_fn)
# df.to_excel(writer, index=False)
# writer.save()
# print("Export to excel file", excel_fn)


class tester_rpt():
    def __init__(self, file_name, options=None):
        self.file_name = file_name
        self.data = None
        if options is not None:
            self.verbose = options.verbose
        else:
            self.verbose = True
        self.failed_bump = dict()
        self.parse()

    def parse(self):
        all_data = []
        if self.verbose:
            print("Parsing File", self.file_name, "...")
            print("These line is not parsed by this program: ")
            print("------------------------------------------------------------------")
        with open(self.file_name) as fp:
            for line in fp:
                m = rPassPat.search(line)
                if m:
                    la = list(m.groups())
                    la.insert(9, ' ')  # make it the same length, with Pass flag
                    all_data.append(la)
                    continue

                m = rFailPat.search(line)
                if m:
                    all_data.append(list(m.groups()))
                    # Logging entry of failed bump
                    name = m.group(4)
                    status = m.group(10)
                    if name in self.failed_bump:
                        self.failed_bump[name].append(status)
                    else:
                        self.failed_bump[name] = [status]
                    continue
                if self.verbose:
                    print(line.rstrip())
        self.data = pd.DataFrame(all_data, columns=header)

    def write_excel(self, out_name=None):
        if out_name:
            excel_fn = out_name
        else:
            base, ext = os.path.splitext(self.file_name)
            excel_fn = base + '.xlsx'
        writer = pd.ExcelWriter(excel_fn)
        self.data.to_excel(writer, index=False)
        writer.save()
        if self.verbose:
            print("Export to excel file", excel_fn)


if __name__ == '__main__':
    usage = "usage: %prog [options] logfile1 logfile2"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-v', '--verbose',
                      dest="verbose",
                      default=False,
                      action="store_true",
                      help='show verbose message'
                      )

    options, remainder = parser.parse_args()
    for fn in remainder:
        test = tester_rpt(fn, options)
        test.write_excel()
        for key, value in test.failed_bump.items():
            print(key, value)