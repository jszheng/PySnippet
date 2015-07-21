# -*- coding: utf-8 -*-
"""单选框示例"""
import sys
from PyQt5 import QtWidgets, QtCore


class CheckBox(QtWidgets.QWidget):
    def __init__(self):
        super(CheckBox, self).__init__()

        self.setWindowTitle("单选框演示程序")
        self.setGeometry(300, 300, 250, 150)

        self.check_box = QtWidgets.QCheckBox("显示标题", self)
        self.check_box.move(10, 10)
        self.check_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.check_box.toggle()
        self.check_box.stateChanged.connect(self.change_title)

    def change_title(self):
        if self.check_box.isChecked():
            self.setWindowTitle("单选框演示程序")
        else:
            self.setWindowTitle("单选框未选中")

app = QtWidgets.QApplication(sys.argv)
cb = CheckBox()
cb.show()
sys.exit(app.exec_())