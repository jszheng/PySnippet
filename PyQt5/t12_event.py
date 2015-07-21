# -*- coding: utf-8 -*-
"""用Esc键推出示例"""
import sys
from PyQt5 import QtWidgets, QtCore

class Escape(QtWidgets.QWidget):
    def __init__(self):
        super(Escape, self).__init__()

        self.setWindowTitle("Esc退出演示程序")
        self.resize(250, 150)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

app = QtWidgets.QApplication(sys.argv)
escape = Escape()
escape.show()
sys.exit(app.exec_())
