# -*- coding: utf-8 -*-
"""滑块和标签示例"""
import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class SliderLabel(QtWidgets.QWidget):
    def __init__(self):
        super(SliderLabel, self).__init__()

        self.setWindowTitle("滑块和标签演示程序")
        self.setGeometry(300, 300, 300, 200)

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setGeometry(30, 40, 100, 30)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.valueChanged.connect(self.change_value)

        self.label = QtWidgets.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap(r"sample_06.png"))
        self.label.setGeometry(160, 40, 128, 128)

    def change_value(self):
        pos = self.slider.value()
        if pos == 0:
            self.label.setPixmap(QtGui.QPixmap(r"sapmle_06.png"))
        elif 0 < pos < 60:
            self.label.setPixmap(QtGui.QPixmap(r"sapmle__12.png"))
        else:
            self.label.setPixmap(QtGui.QPixmap(r"sapmle__05.png"))

app = QtWidgets.QApplication(sys.argv)
sl = SliderLabel()
sl.show()
sys.exit(app.exec_())
