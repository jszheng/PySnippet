import sys
import os
import re
import pickle
import time

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class LongJob(QThread):
    result_ready = pyqtSignal()

    def __init__(self):
        self.mutex = QMutex()
        self.cond = QWaitCondition()
        self.restart = False
        self.abort = False

    def __del__(self):
        self.mutex.lock()
        self.abort = True
        self.cond.wakeOne()
        self.mutex.unlock()
        self.wait()

    def run(self):
        time.sleep(5)
