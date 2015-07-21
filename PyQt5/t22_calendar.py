# -*- coding: utf-8 -*-
"""日历部件示例"""
import sys
from PyQt5 import QtWidgets, QtCore


class CalendarWidget(QtWidgets.QWidget):
    def __init__(self):
        super(CalendarWidget, self).__init__()

        self.setWindowTitle("日历部件演示程序")
        self.setGeometry(300, 300, 350, 300)

        self.calendar = QtWidgets.QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.show_date)

        date = self.calendar.selectedDate()
        self.label = QtWidgets.QLabel(self)
        self.label.setText(str(date.toPyDate()))

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.calendar)
        v_box.addWidget(self.label)
        self.setLayout(v_box)

    def show_date(self):
        date = self.calendar.selectedDate()
        self.label.setText(str(date.toPyDate()))

app = QtWidgets.QApplication(sys.argv)
cw = CalendarWidget()
cw.show()
sys.exit(app.exec_())
