from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

if __name__ == '__main__':
    print('open from CRM_main.py')

class TopLevelCrear(QWidget):
    '''configuracion de la ventana de crear database'''
    def setupUi(self,crear_db,MainWindowCommands,direction_label,tree):
        crear_db.setObjectName("crear_db")
        crear_db.setWindowTitle('Crear DB')
        crear_db.resize(184, 103)
        crear_db.setMaximumSize(QtCore.QSize(250, 140))
        crear_db.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.gridLayout = QtWidgets.QGridLayout(crear_db)
        self.gridLayout.setObjectName("gridLayout")

        #layout principal
        self.crear_layout = QtWidgets.QVBoxLayout()
        self.crear_layout.setObjectName("crear_layout")
        #Label
        self.crear_label = QtWidgets.QLabel('Nombre de la base de datos',crear_db)
        self.crear_label.setObjectName("crear_label")
        self.crear_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.crear_layout.addWidget(self.crear_label, 0, QtCore.Qt.AlignHCenter)
        #Entry
        self.crear_entry = QtWidgets.QLineEdit(crear_db)
        self.crear_entry.setObjectName("crear_entry")
        self.crear_entry.setStyleSheet("color: rgb(255, 255, 255);")
        self.crear_layout.addWidget(self.crear_entry)
        #Button
        self.crear_button = QtWidgets.QPushButton('Crear',crear_db,
            clicked=lambda:MainWindowCommands.crear(self,self.crear_entry.text(),direction_label,tree,crear_db))
        self.crear_button.setObjectName("crear_button")
        self.crear_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.517364, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n""color: rgb(255, 255, 255);")
        self.crear_layout.addWidget(self.crear_button, 0, QtCore.Qt.AlignHCenter)

        self.gridLayout.addLayout(self.crear_layout, 0, 0, 1, 1)