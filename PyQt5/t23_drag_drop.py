# -*- coding: utf-8 -*-
"""拖放功能示例"""
import sys
from PyQt5 import QtWidgets


class Button(QtWidgets.QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())


class DragDrop(QtWidgets.QDialog):
    def __init__(self):
        super(DragDrop, self).__init__()

        self.setWindowTitle("拖放功能演示程序")
        self.resize(280, 150)
        edit = QtWidgets.QLineEdit("", self)
        edit.move(30, 65)
        edit.setDragEnabled(True)
        button = Button("按钮", self)
        button.move(170, 65)

        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

app = QtWidgets.QApplication(sys.argv)
dd = DragDrop()
dd.show()
sys.exit(app.exec_())