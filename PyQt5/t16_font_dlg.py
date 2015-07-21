# -*- coding: utf-8 -*-
"""字体对话框示例"""
import sys
from PyQt5 import QtWidgets, QtCore


class FontDialog(QtWidgets.QWidget):
    def __init__(self):
        super(FontDialog, self).__init__()

        self.setWindowTitle("字体对话框示例程序")
        self.setGeometry(300, 300, 250, 110)

        self.button = QtWidgets.QPushButton("对话框", self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)
        self.button.clicked.connect(self.show_dialog)

        self.label = QtWidgets.QLabel("普通的disco我们普通的摇", self)
        self.label.move(130, 30)

        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addWidget(self.button)
        self.h_box.addWidget(self.label, 1)
        self.setLayout(self.h_box)

    def show_dialog(self):
        font, ok = QtWidgets.QFontDialog.getFont(self)
        if ok:
            self.label.setFont(font)

app = QtWidgets.QApplication(sys.argv)
fd = FontDialog()
fd.show()
sys.exit(app.exec_())
