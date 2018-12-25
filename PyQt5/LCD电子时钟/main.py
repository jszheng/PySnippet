'''
Created on 2018-08-09 22:39

@author: Freedom
'''
from PyQt5.QtWidgets import QApplication
import sys
from DigitalClock import DigitalClock

def main():
    
    app = QApplication(sys.argv)
    clock = DigitalClock(None)
    clock.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()