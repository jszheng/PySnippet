__author__ = 'jszheng'

import sys
import os
import re
import pickle

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class ParseProgress(QDialog):
    def __init__(self, parent=None):
        super(ParseProgress, self).__init__(parent)
        self.progress = QProgressBar(self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.progress)
        self.setLayout(self.layout)
        self.setWindowTitle("Parsing Log file ...")

    def setValue(self, value):
        self.progress.setValue(value)

    def setMax(self, value):
        self.progress.setMaximum(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    overwrite = QMessageBox.warning(
        None,
        "Overwrite Pickle File?",
        "Log file %s already parsed! Are you going to parse it again and overwrite the pickle file?" % ('textri.log'),
        QMessageBox.Ok | QMessageBox.No,
        QMessageBox.No
    )
    #print(overwrite==QMessageBox.Ok)

    dlg = ParseProgress()
    print(dlg.progress.isTextVisible())
    dlg.setMax(1290)
    dlg.setValue(1000)
    dlg.show()

    sys.exit(app.exec_())