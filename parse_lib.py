import re

def parse_lib(filename):
    with open(filename, 'r') as fp:
        print("process", filename)
        cell_num = 0
        cell = None
        pin = None
        function = None
        area = 0
        for line in fp:
            m = re.match(r'^\s*cell\s*\((.*)\)\s*\{', line)
            if m:
                cell = m.group(1)
                cell_num += 1
                continue
            m = re.match(r'^\s*area\s*:\s*(.*)\s*;', line)
            if m:
                area = m.group(1)
                print(cell, area)
                continue
            m = re.match(r'^\s*pin\s*\((.*)\)\s*\{', line)
            if m:
                pin = m.group(1)
                continue
            m = re.match(r'^\s*function\s*:\s*(.*)\s*;', line)
            if m:
                function = m.group(1)
                print(pin, function)
                continue


    print('Total', cell_num, 'cells found!')

if __name__ == '__main__':
    file = "D:/Downloads/EDA_Install/Synopsys DesignWare Logic Library TSMC 28HPC SVT ts28nchslogl35hdl140f/ts28nchslogl35hdl140h_liberty_basic_v02/liberty/logic_synth/ts28nchslogl35hdl140f_ffbc0p99v125c.lib"
    parse_lib(file)