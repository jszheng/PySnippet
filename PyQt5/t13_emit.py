# -*- coding: utf-8 -*-
"""发射信号示例"""
import sys
from PyQt5 import QtWidgets, QtCore


class EmitSignal(QtWidgets.QWidget):
    closeEmitApp = QtCore.pyqtSignal()

    def __init__(self):
        super(EmitSignal, self).__init__()

        self.setWindowTitle("发射信号演示程序")
        self.resize(250, 150)

        self.closeEmitApp.connect(self.close)

    def mousePressEvent(self, QMouseEvent):
        self.closeEmitApp.emit()

app = QtWidgets.QApplication(sys.argv)
es = EmitSignal()
es.show()
sys.exit(app.exec_())
