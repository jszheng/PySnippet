# -*-coding:utf-8-*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

import sys
import os
import re
from parse_log import *


class FilterWindow(QDialog):
    def __init__(self, parent=None):
        super(FilterWindow, self).__init__(parent)
        self.fileLabel = QLabel("Bump File :")
        self.fileLineEdit = QLineEdit()
        self.browseButton = QPushButton("Browse...")

        self.colLabel = QLabel("Columns :")
        self.colComboBox = self.createComboBox()
        self.colButton = QPushButton("Parse...")

        self.filterLabel = QLabel("Filter :")
        self.filterComboBox = self.createComboBox(".*")
        self.filterButton = QPushButton("Filter...")

        self.testLabel = QLabel("Test Report :")
        self.testLineEdit = QLineEdit()
        self.testButton = QPushButton("Browse...")

        self.tcolLabel = QLabel("Columns :")
        self.tcolComboBox = self.createComboBox()
        self.tcolButton = QPushButton("Parse...")

        self.tfilterLabel = QLabel("Filter :")
        self.tfilterComboBox = self.createComboBox(".*")
        self.tfilterButton = QPushButton("Filter...")

        self.bumpList = QListWidget()
        self.testerList = QListWidget()

        frameStyle = QFrame.Sunken | QFrame.Panel
        self.colorButton = QPushButton("Color")
        self.colorLabel = QLabel()
        self.colorLabel.setFrameStyle(frameStyle)

        self.clearButton = QPushButton("Clear")
        self.drawButton = QPushButton("Draw Orig")
        self.drawTesterButton = QPushButton("Draw Tester")

        bumpLayout = QGridLayout()
        bumpLayout.addWidget(self.fileLabel, 0, 0)
        bumpLayout.addWidget(self.fileLineEdit, 0, 1)
        bumpLayout.addWidget(self.browseButton, 0, 2)

        bumpLayout.addWidget(self.colLabel, 1, 0)
        bumpLayout.addWidget(self.colComboBox, 1, 1)
        bumpLayout.addWidget(self.colButton, 1, 2)

        bumpLayout.addWidget(self.filterLabel, 2, 0)
        bumpLayout.addWidget(self.filterComboBox, 2, 1)
        bumpLayout.addWidget(self.filterButton, 2, 2)

        testerLayout = QGridLayout()
        testerLayout.addWidget(self.testLabel, 0, 0)
        testerLayout.addWidget(self.testLineEdit, 0, 1)
        testerLayout.addWidget(self.testButton, 0, 2)

        testerLayout.addWidget(self.tcolLabel, 1, 0)
        testerLayout.addWidget(self.tcolComboBox, 1, 1)
        testerLayout.addWidget(self.tcolButton, 1, 2)

        testerLayout.addWidget(self.tfilterLabel, 2, 0)
        testerLayout.addWidget(self.tfilterComboBox, 2, 1)
        testerLayout.addWidget(self.tfilterButton, 2, 2)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(bumpLayout)
        mainLayout.addWidget(self.bumpList)
        mainLayout.addLayout(testerLayout)
        mainLayout.addWidget(self.testerList)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.colorButton)
        hLayout.addWidget(self.colorLabel)
        hLayout.addWidget(self.drawButton)
        hLayout.addWidget(self.drawTesterButton)
        hLayout.addWidget(self.clearButton)

        mainLayout.addLayout(hLayout)
        self.setLayout(mainLayout)
        self.setWindowTitle("Bump Draw")
        self.resize(700, 800)

        # Connect Actions
        self.browseButton.clicked.connect(self.browse)
        self.colButton.clicked.connect(self.parse_bump_file)
        self.filterButton.clicked.connect(self.filter_bump)
        self.testButton.clicked.connect(self.browse_test_rpt)
        self.tcolButton.clicked.connect(self.parse_test_rpt)
        self.tfilterButton.clicked.connect(self.filter_test)
        self.colorButton.clicked.connect(self.setColor)
        self.drawButton.clicked.connect(self.drawOriginal)
        self.drawTesterButton.clicked.connect(self.drawTester)
        self.clearButton.clicked.connect(self.clear_draw)

        # Datas
        self.bump_df = None
        self.tester_df = None

        self.currentDir = QDir.currentPath()

    def createComboBox(self, text=""):
        comboBox = QComboBox()
        comboBox.setEditable(True)
        comboBox.addItem(text)
        comboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        return comboBox

    def browse(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "Bump File",  # Caption
            self.currentDir,
            "Excel Files (*.xls *.xlsx);;All Files (*)")
        if fileName:
            self.fileLineEdit.setText(fileName)
            self.currentDir = os.path.dirname(fileName)

    def parse_bump_file(self):
        filename = self.fileLineEdit.text()
        if not os.path.isfile(filename):
            return
        print("Parsing bump file", filename)
        self.bump_df = pd.DataFrame(pd.read_excel(filename, sheet_name='4-2.HW PA'))
        # self.x = self.bump_df['BumpX\n(Tester View)'].values.tolist()
        # self.y = self.bump_df['BumpY\n(Tester View)'].values.tolist()
        # self.name = self.bump_df['Bump Name'].values.tolist()
        columns = self.bump_df.columns.values.tolist()
        self.colComboBox.clear()
        for c in columns:
            self.colComboBox.addItem(c)
        self.colComboBox.setCurrentIndex(3)
        print("Done!")

    def filter_bump(self):
        # colIndex = self.colComboBox.currentIndex()
        colName = self.colComboBox.currentText()
        filterStr = self.filterComboBox.currentText()
        # print(colName)
        # print(filterStr)
        # print(self.bump_df)

        # df_filtered = self.bump_df[self.bump_df[colName].str.match(filterStr) == True]
        # data_list = df_filtered[colName].values.tolist()

        # not stable, using seperate steps
        colData = self.bump_df[colName].values.tolist()
        try:  # do not exit program when input regular express failed compilation
            r = re.compile(filterStr)
        except:
            return
        data_list = list(filter(r.match, colData))
        print("found", len(data_list), "data")

        # print(df_filtered)
        # print(len(data_list))
        # print(data_list)
        # print(type(data_list))
        self.bumpList.clear()
        self.bumpList.addItems(data_list)

    def browse_test_rpt(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "Test Report File",  # Caption
            self.currentDir,
            "Log Files (*.txt);;All Files (*)")
        if fileName:
            self.testLineEdit.setText(fileName)
            self.currentDir = os.path.dirname(fileName)

    def parse_test_rpt(self):
        filename = self.testLineEdit.text()
        if not os.path.isfile(filename):
            return
        print("Parsing test file", filename)
        self.tf = tester_rpt(filename)
        self.tester_df = self.tf.data
        columns = self.tester_df.columns.values.tolist()
        self.tcolComboBox.clear()
        for c in columns:
            self.tcolComboBox.addItem(c)
        self.tcolComboBox.setCurrentIndex(3)
        print("Done!")

    def filter_test(self):
        colName = self.tcolComboBox.currentText()
        filterStr = self.tfilterComboBox.currentText()
        colData = self.tester_df[colName].values.tolist()
        print(colName)
        print(filterStr)
        print(colData)
        try:  # do not exit program when input regular express failed compilation
            r = re.compile(filterStr)
        except:
            return
        data_list = list(filter(r.match, colData))
        print(data_list)
        print(len(data_list))
        print("found", len(data_list), "data")

        self.testerList.clear()
        self.testerList.addItems(data_list)

    def setColor(self):
        color = QColorDialog.getColor(Qt.green, self)
        if color.isValid():
            self.colorLabel.setText(color.name())
            self.colorLabel.setPalette(QPalette(color))
            self.colorLabel.setAutoFillBackground(True)

    def drawOriginal(self):
        print("TODO: Draw Original Pin Location")
        pass

    def drawTester(self):
        print("TODO : Draw Tester Report")
        pass

    def clear_draw(self):
        print("TODO: clear current draw screen")
        pass


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


class BumpViewWindows(QDialog):
    def __init__(self, parent=None):
        super(BumpViewWindows, self).__init__(parent)
        self.setWindowTitle("Bump Map")
        self.resize(1024, 960)

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)

        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(self.canvas)
        self.setLayout(self.hlayout)
        self.plot()

    def plot(self):
        try:
            ax = self.fig.add_subplot(111)
            #ax.scatter([0], [0], 'r')
            #x = np.linspace(0, 100, 100)
            #y = np.random.random(100)
            ax.cla()
            ax.set_aspect('equal')
            ax.set_title("BI Bump Map")
            ax.set_xlabel("Y")
            ax.set_ylabel("X")
            scale = 1.1
            zp = ZoomPan()
            figZoom = zp.zoom_factory(ax, base_scale=scale)
            figPan = zp.pan_factory(ax)
            #ax.plot(x, y)
            import pickle
            with open('bump_info.dat', 'rb') as pk:
                sig_x, sig_y, scan_x, scan_y, vdd_x, vdd_y, vss_x, vss_y = pickle.load(pk)

            print('VDD     ', len(vdd_x), len(vdd_y))
            print('VSS     ', len(vss_x), len(vss_y))
            print('scan    ', len(scan_x), len(scan_y))
            print('Signals ', len(sig_x), len(sig_y))

            ax.scatter(sig_y, sig_x)
            ax.scatter(scan_y, scan_x, c='g')
            ax.scatter(vdd_y, vdd_x, c='#200000')
            ax.scatter(vss_y, vss_x, c='#d0d0d0')
            ax.scatter(vss_y, vss_x, c='#d0d0d0')

            self.canvas.draw()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fw = FilterWindow()
    fw.show()
    bv = BumpViewWindows()
    bv.show()
    sys.exit(app.exec_())
