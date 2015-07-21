# -*- coding: utf-8 -*-
"""进度条示例"""
import sys
from PyQt5 import QtWidgets, QtCore


class ProgressBar(QtWidgets.QWidget):
    def __init__(self):
        super(ProgressBar, self).__init__()

        self.setWindowTitle("进度条演示程序")
        self.setGeometry(300, 300, 250, 150)

        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setGeometry(30, 40, 200, 25)

        self.button = QtWidgets.QPushButton("开始", self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(40, 80)
        self.button.clicked.connect(self.on_start)

        self.timer = QtCore.QBasicTimer()
        self.step = 0

    def timerEvent(self, *args, **kwargs):
        if self.step >= 100:
            self.timer.stop()
            self.button.setText("重新开始")
            return
        self.step += 1
        self.progress_bar.setValue(self.step)

    def on_start(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText("开始")
        else:
            self.timer.start(100, self)
            self.button.setText("停止")

app = QtWidgets.QApplication(sys.argv)
pb = ProgressBar()
pb.show()
sys.exit(app.exec_())
