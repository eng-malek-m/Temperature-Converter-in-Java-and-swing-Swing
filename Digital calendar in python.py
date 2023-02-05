import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QCalendarWidget

app = QApplication(sys.argv)

cal = QCalendarWidget()
cal.setGridVisible(True)
cal.setMinimumDate(QDate(1900, 1, 1))
cal.setMaximumDate(QDate(2100, 1, 1))
cal.setSelectedDate(QDate.currentDate())
cal.setFirstDayOfWeek(Qt.Monday)
cal.show()

sys.exit(app.exec_())
