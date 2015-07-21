__author__ = 'jszheng'

import sys
import time

from PyQt5 import QtWidgets, QtCore

from first import Ui_MainWindow


class mySignalSlot(QtWidgets.QMainWindow, Ui_MainWindow):
    my_sig = QtCore.pyqtSignal(str)

    def __init__(self):
        super(mySignalSlot, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.prn)
        self.pushButton_2.clicked.connect(self.prn2)
        self.my_sig.connect(self.myslot)

    def prn(self):
        print("prn clicked")
        print("sleep(1)")
        time.sleep(1)
        self.my_sig.emit('button1')

    def prn2(self):
        print("prn clicked")
        print("sleep(3)")
        time.sleep(1)
        self.my_sig.emit('button2')

    def myslot(self, para):
        print("myslot tiggered : ", para)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = mySignalSlot()
    my.show()
    sys.exit(app.exec_())
