# -*- coding: utf-8 -*-
# using matplotlib with PyQT5

# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
# import sys
# import numpy as np
import pandas as pd
import re

# Using Matplotlib
# import matplotlib
#
# matplotlib.use("Qt5Agg")  # 声明使用QT5
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# read the data
bump_file = '/home/jszheng/Downloads/XY coordinates and pin assignment.xlsx'
df = pd.DataFrame(pd.read_excel(bump_file, sheet_name='4-2.HW PA'))
# print(df.head())
# print(df['BumpX\n(Tester View)'].values.tolist())
x = df['BumpX\n(Tester View)'].values.tolist()
y = df['BumpY\n(Tester View)'].values.tolist()
names = df['Bump Name'].values.tolist()

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

for key, value in name_cnt.items():
    if value > 1:
        print(key, "\t\t\t", value)

# col_names = df.columns.values.tolist()
# print(col_names)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_title("BI Bump Map")
ax.set_xlabel("Y")
ax.set_ylabel("X")


# base on
# https://stackoverflow.com/questions/11551049/matplotlib-plot-zooming-with-scroll-wheel
def zoom_factory(ax, base_scale=2.):
    def zoom_fun(event):
        # get the current x and y limits
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        cur_xrange = (cur_xlim[1] - cur_xlim[0]) * .5
        cur_yrange = (cur_ylim[1] - cur_ylim[0]) * .5
        xdata = event.xdata  # get event x location
        ydata = event.ydata  # get event y location
        if event.button == 'up':
            # deal with zoom in
            scale_factor = 1 / base_scale
        elif event.button == 'down':
            # deal with zoom out
            scale_factor = base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1
            print(event.button)
        # set new limits
        ax.set_xlim([xdata - cur_xrange * scale_factor,
                     xdata + cur_xrange * scale_factor])
        ax.set_ylim([ydata - cur_yrange * scale_factor,
                     ydata + cur_yrange * scale_factor])
        plt.draw()  # force re-draw

    fig = ax.get_figure()  # get the figure of interest
    # attach the call back
    fig.canvas.mpl_connect('scroll_event', zoom_fun)

    # return the function
    return zoom_fun


class ZoomPan:
    def __init__(self):
        self.press = None
        self.cur_xlim = None
        self.cur_ylim = None
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.xpress = None
        self.ypress = None

    def zoom_factory(self, ax, base_scale=2.):
        def zoom(event):
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()

            xdata = event.xdata  # get event x location
            ydata = event.ydata  # get event y location

            if event.button == 'down':
                # deal with zoom in
                scale_factor = 1 / base_scale
            elif event.button == 'up':
                # deal with zoom out
                scale_factor = base_scale
            else:
                # deal with something that should never happen
                scale_factor = 1
                print(event.button)

            new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

            relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
            rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])

            ax.set_xlim([xdata - new_width * (1 - relx), xdata + new_width * (relx)])
            ax.set_ylim([ydata - new_height * (1 - rely), ydata + new_height * (rely)])
            ax.figure.canvas.draw()

        fig = ax.get_figure()  # get the figure of interest
        fig.canvas.mpl_connect('scroll_event', zoom)

        return zoom

    def pan_factory(self, ax):
        def onPress(event):
            if event.inaxes != ax: return
            self.cur_xlim = ax.get_xlim()
            self.cur_ylim = ax.get_ylim()
            self.press = self.x0, self.y0, event.xdata, event.ydata
            self.x0, self.y0, self.xpress, self.ypress = self.press

        def onRelease(event):
            self.press = None
            ax.figure.canvas.draw()

        def onMotion(event):
            if self.press is None: return
            if event.inaxes != ax: return
            dx = event.xdata - self.xpress
            dy = event.ydata - self.ypress
            self.cur_xlim -= dx
            self.cur_ylim -= dy
            ax.set_xlim(self.cur_xlim)
            ax.set_ylim(self.cur_ylim)

            ax.figure.canvas.draw()

        fig = ax.get_figure()  # get the figure of interest

        # attach the call back
        fig.canvas.mpl_connect('button_press_event', onPress)
        fig.canvas.mpl_connect('button_release_event', onRelease)
        fig.canvas.mpl_connect('motion_notify_event', onMotion)

        # return the function
        return onMotion


# scale = 1.2
# f = zoom_factory(ax, base_scale=scale)

scale = 1.1
zp = ZoomPan()
figZoom = zp.zoom_factory(ax, base_scale=scale)
figPan = zp.pan_factory(ax)

# draw all bump
# ax.scatter(y, x)
# print(len(x), len(y))

# remove power
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

print('Total', len(x), len(y))
print('VDD', len(vdd_x), len(vdd_y))
print('VSS', len(vss_x), len(vss_y))
print('scan', len(scan_x), len(scan_y))
print('Signals ', other, len(sig_x), len(sig_y))
ax.scatter(vdd_y, vdd_x, c='#400000')
ax.scatter(vss_y, vss_x, c='#e0e0e0')
ax.scatter(scan_y, scan_x, c='g')
ax.scatter(sig_y, sig_x)

# Mark Failed
from parse_log import *

testfile = tester_rpt('/home/jszheng/Downloads/log_0920_x0y0_new_IO.txt')
hx = []
hy = []
for key, value in testfile.failed_bump.items():
    if key in name:
        index = name.index(key)
        hx.append(x[index])
        hy.append(y[index])
    else:
        print(key, "not in the BI bump list, please check!")
ax.scatter(hy, hx, c='r', marker='x')

plt.show()
