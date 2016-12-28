import re
import pickle
import json
import os

def parse_lib(filename):
    re_cell = re.compile(r'^\s*cell\s*\("(.*)"\)\s*\{')
    re_area = re.compile(r'^\s*area\s*:\s*(.*)\s*;')
    re_pin = re.compile(r'^\s*pin\s*\((.*)\)\s*\{')
    re_dir = re.compile(r'^\s*direction\s*:\s*"(.*)"\s*;')
    re_func= re.compile(r'^\s*function\s*:\s*"(.*)"\s*;')

    cell_num = 0

    cell = None
    pin = None
    function = None
    area = None
    direction = None

    std_cells = []
    ports = []

    std_cell = {}
    current_cell = None
    port ={}
    current_port = None

    with open(filename, 'r') as fp:
        print("process", filename)
        for line in fp:
            m = re_cell.match(line)
            if m:
                cell = m.group(1)
                cell_num += 1
                print('found ', cell)
                ports = []
                std_cell = {'name' : cell,
                            'ports' : ports}
                current_cell = std_cell
                std_cells.append(std_cell)
                continue
            if current_cell is None:
                continue
            m = re_area.match(line)
            if m:
                area = m.group(1)
                current_cell['area'] = area
                continue
            m = re_pin.match(line)
            if m:
                pin = m.group(1)
                port = {'name': pin}
                ports.append(port)
                current_port = port
                continue
            m = re_dir.match(line)
            if m:
                direction = m.group(1)
                current_port['direction'] = direction
                continue
            m = re_func.match(line)
            if m:
                function = m.group(1)
                current_port['function'] = function
                continue


    print('Total', cell_num, 'cells found!')
    #from pprint import pprint
    #pprint(std_cells)
    trunk, ext = os.path.splitext(os.path.basename(filename))
    pickle_name = trunk + '.pickle'
    json_name = trunk + '.json'
    with open(pickle_name, 'wb') as fp:
        pickle.dump(std_cells, fp)
    with open(json_name, 'wt') as fp:
        json.dump(std_cells, fp)

if __name__ == '__main__':
    filename = "D:/Downloads/EDA_Install/Synopsys DesignWare Logic Library TSMC 28HPC SVT ts28nchslogl35hdl140f/ts28nchslogl35hdl140h_liberty_basic_v02/liberty/logic_synth/ts28nchslogl35hdl140f_ffbc0p99v125c.lib"


    parse_lib(filename)