# -*- coding: utf-8 -*-
"""颜色对话框示例"""
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class ColorDialog(QtWidgets.QWidget):
    def __init__(self):
        super(ColorDialog, self).__init__()

        self.setWindowTitle("颜色对话框演示程序")
        self.setGeometry(300, 300, 250, 180)

        self.button = QtWidgets.QPushButton("更改颜色", self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)

        self.button.clicked.connect(self.show_dialog)
        self.setFocus()

        color = QtGui.QColor(0, 0, 0)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setStyleSheet("QWidget{background-color:%s}"% color.name())
        self.widget.setGeometry(130, 22, 100, 100)

    def show_dialog(self):
        col = QtWidgets.QColorDialog.getColor()
        if col.isValid():
            self.widget.setStyleSheet("QWidget{background-color:%s}" % col.name())

app = QtWidgets.QApplication(sys.argv)
colordialog = ColorDialog()
colordialog.show()
sys.exit(app.exec_())