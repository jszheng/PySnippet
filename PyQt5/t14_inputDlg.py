# -*- coding: utf-8 -*-
"""输入对话框示例"""
import sys
from PyQt5 import QtWidgets, QtCore

class InputDialog(QtWidgets.QWidget):
    def __init__(self):
        super(InputDialog, self).__init__()

        self.setWindowTitle("输入对话框演示程序")
        self.setGeometry(300, 300, 350, 80)
        self.button = QtWidgets.QPushButton("对话框", self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)
        self.button.clicked.connect(self.show_dialog)
        self.setFocus()

        self.label = QtWidgets.QLineEdit(self)
        self.label.move(130, 22)

    def show_dialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, "输入对话框", "请输入你的名字：")
        if ok:
            self.label.setText(text)

app = QtWidgets.QApplication(sys.argv)
input_dialog = InputDialog()
input_dialog.show()
sys.exit(app.exec_())