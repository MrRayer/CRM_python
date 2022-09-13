from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

if __name__ == '__main__':
    print('open from CRM_main.py')

class TopLevelLog(object):
    '''configuracion de la ventana del registro'''
    def setupUi(self, log_window):
        log_window.setWindowTitle('Registro de actividad')
        log_window.setObjectName("log_window")
        log_window.resize(360, 600)
        log_window.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.gridLayout = QtWidgets.QGridLayout(log_window)
        self.gridLayout.setObjectName("gridLayout")

        self.log_table = QtWidgets.QTableWidget(log_window)
        self.log_table.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(21, 21, 21, 255), stop:1 rgba(62, 62, 62, 255));\n""color: rgb(255, 255, 255);")
        style = "::section {""background-color:rgb(44, 44, 44); }"
        self.log_table.horizontalHeader().setStyleSheet(style)
        self.log_table.verticalHeader().setVisible(False)
        self.log_table.setObjectName("log_table")
        self.log_table.setColumnCount(5)
        self.log_table.setRowCount(0)
        self.log_table.setHorizontalHeaderLabels(['id','Evento','ida','Fecha','Hora'])
        self.log_table.resizeColumnsToContents()
        self.log_table.setColumnWidth(0,10)
        self.log_table.setColumnWidth(1,50)
        self.log_table.setColumnWidth(2,75)
        self.log_table.setColumnWidth(3,75)
        self.log_table.setColumnWidth(4,75)
        self.log_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.gridLayout.addWidget(self.log_table, 0, 0, 1, 1)

        return self.log_table

    def return_log():
        return self.log_table