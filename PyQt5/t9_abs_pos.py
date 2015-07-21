# -*- coding: utf-8 -*-
"""绝对定位演示"""

import sys
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("绝对定位演示程序")
        self.resize(250, 150)
        QtWidgets.QLabel('Couldn\'t', self).move(15, 10)
        QtWidgets.QLabel('care', self).move(35, 40)
        QtWidgets.QLabel('less', self).move(55, 65)
        QtWidgets.QLabel('and', self).move(115, 65)
        QtWidgets.QLabel('then', self).move(135, 45)
        QtWidgets.QLabel('you', self).move(115, 25)
        QtWidgets.QLabel('kiss', self).move(145, 10)
        QtWidgets.QLabel('me', self).move(215, 10)

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
