# -*- coding: utf-8 -*-
"""开关按钮示例"""
import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class ToggleButton(QtWidgets.QWidget):
    def __init__(self):
        super(ToggleButton, self).__init__()

        self.setWindowTitle("开关按钮演示程序")
        self.setGeometry(300, 300, 280, 170)

        self.red = QtWidgets.QPushButton("红", self)
        self.red.setCheckable(True)
        self.red.move(10, 10)
        self.red.clicked.connect(self.set_red)

        self.green = QtWidgets.QPushButton("绿", self)
        self.green.setCheckable(True)
        self.green.move(10, 60)
        self.green.clicked.connect(self.set_green)

        self.blue = QtWidgets.QPushButton("蓝", self)
        self.blue.setCheckable(True)
        self.blue.move(10, 110)
        self.blue.clicked.connect(self.set_blue)

        self.square = QtWidgets.QWidget(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.color = QtGui.QColor(0, 0, 0)
        self.square.setStyleSheet("QWidget{background-color:%s}" % self.color.name())

        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create("cleanlooks"))

    def set_red(self):
        if self.red.isChecked():
            self.color.setRed(255)
        else:
            self.color.setRed(0)
        self.square.setStyleSheet("QWidget{background-color:%s}" % self.color.name())

    def set_green(self):
        if self.green.isChecked():
            self.color.setGreen(255)
        else:
            self.color.setGreen(0)
        self.square.setStyleSheet("QWidget{background-color:%s}" % self.color.name())

    def set_blue(self):
        if self.blue.isChecked():
            self.color.setBlue(255)
        else:
            self.color.setBlue(0)
        self.square.setStyleSheet("QWidget{background-color:%s}" % self.color.name())

app = QtWidgets.QApplication(sys.argv)
tb = ToggleButton()
tb.show()
sys.exit(app.exec_())
