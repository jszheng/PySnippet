# -*- coding: utf-8 -*-
"""信号槽示例"""

import sys
from PyQt5 import QtWidgets, QtCore


class SignalSlot(QtWidgets.QWidget):
    def __init__(self):
        super(SignalSlot, self).__init__()

        self.setWindowTitle("信号槽演示程序")
        lcd = QtWidgets.QLCDNumber(self)
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(lcd)
        v_box.addWidget(slider)

        self.setLayout(v_box)
        slider.valueChanged.connect(lcd.display)
        self.resize(250, 150)

app = QtWidgets.QApplication(sys.argv)
qb = SignalSlot()
qb.show()
sys.exit(app.exec_())
