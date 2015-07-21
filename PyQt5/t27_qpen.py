# -*- coding: utf-8 -*-
"""QPen示例"""
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Brush(QtWidgets.QWidget):
    def __init__(self):
        super(Brush, self).__init__()

        self.setWindowTitle("QPen演示程序")
        self.setGeometry(300, 300, 280, 270)

    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)

        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)

        paint.setPen(pen)
        paint.drawLine(20, 40, 250, 40)

        pen.setStyle(QtCore.Qt.DashLine)
        paint.setPen(pen)
        paint.drawLine(20, 80, 250, 80)

        pen.setStyle(QtCore.Qt.DashDotLine)
        paint.setPen(pen)
        paint.drawLine(20, 120, 250, 120)

        pen.setStyle(QtCore.Qt.DotLine)
        paint.setPen(pen)
        paint.drawLine(20, 160, 250, 160)

        pen.setStyle(QtCore.Qt.DashDotDotLine)
        paint.setPen(pen)
        paint.drawLine(20, 200, 250, 200)

        pen.setStyle(QtCore.Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        paint.setPen(pen)
        paint.drawLine(20, 240, 250, 240)

        paint.end()
app = QtWidgets.QApplication(sys.argv)
ps = Brush()
ps.show()
sys.exit(app.exec_())
