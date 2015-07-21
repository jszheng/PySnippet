import sys
from PyQt4 import QtGui, QtCore


class demowind(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Demo Window')
        pbquit = QtGui.QPushButton('Close', self)
        pbquit.setGeometry(10, 10, 70, 40)
        self.connect(pbquit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))


app = QtGui.QApplication(sys.argv)
dw = demowind()
dw.show()
sys.exit(app.exec_())