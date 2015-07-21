# -*- coding: utf-8 -*-
"""拖放按钮示例"""
import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class Button(QtWidgets.QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

    def mouseMoveEvent(self, event):
        if event.buttons() != QtCore.Qt.RightButton:
            return
        mime_data = QtCore.QMimeData()
        drag = QtGui.QDrag(self)
        drag.setMimeData(mime_data)
        drag.setHotSpot(event.pos()-self.rect().topLeft())
        drop_action = drag.exec_(QtCore.Qt.MoveAction)
        if drop_action == QtCore.Qt.MoveAction:
            self.close()

    def mousePressEvent(self, event):
        QtWidgets.QPushButton.mousePressEvent(self, event)
        if event.button() == QtCore.Qt.LeftButton:
            print("按下")


class DragButton(QtWidgets.QDialog):
    def __init__(self):
        super(DragButton, self).__init__()
        self.setWindowTitle("拖放按钮演示程序")
        self.resize(280, 150)
        self.setAcceptDrops(True)
        self.button = Button("关闭", self)
        self.button.move(100, 65)

        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        position = event.pos()
        button = Button("关闭", self)
        button.move(position)
        button.show()
        event.setDropAction(QtCore.Qt.MoveAction)
        event.accept()
app = QtWidgets.QApplication(sys.argv)
db = DragButton()
db.show()
sys.exit(app.exec_())