# coding=utf-8
import re

file_path = 'D:/work/sources/MS_COCO/Microsoft_COCO_reference.txt'

# one liner
with open(file_path, 'r') as file:
    hold_line = None
    for line in file:
        if re.match(r'^\[\d+\]', line):  #start of line
            if hold_line is not None:
                print(hold_line)
            hold_line = line.strip()
        else:
            if hold_line is not None:
                hold_line += ' ' + line.strip()
            else:
                print(line)
    # before exist, print last
    if hold_line is not None:
        print(hold_line)
