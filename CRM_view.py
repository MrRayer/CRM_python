from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence
import PyQt5.QtGui as qtg
from CRM_crear_widget import TopLevelCrear
from CRM_log_widget import TopLevelLog
#from CRM_title_bar import *

if __name__ == '__main__':
	print('open from CRM_main.py')

def load_error(self=None):
	'''messagebox de pyqt5, da una ventana de error'''
	print('error: direccion=None, debe cargar una direccion usando el comando abrir o crear')
	QtWidgets.QMessageBox.about(self,'DB no cargada','Abra su DB antes de continuar')

def custom_error(title,message,self=None):
	'''messagebox de pyqt5, da una ventana de error'''
	print(f'custom_error: {title}, {message}')
	QtWidgets.QMessageBox.about(self,title,message)

class MainWindowWidgets(object):
	'''Config de la ventana principal'''
	def setupUi(self, main_window,MainWindowCommands,font=('Comic Sans MS',9)):
		main_window.setWindowTitle('CRMaster9000')
		#main_window.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		main_window.setObjectName("main_window")
		main_window.resize(689, 497)
		main_window.setStyleSheet("background-color: rgb(40, 40, 40);")

		self.centralwidget = QtWidgets.QWidget(main_window)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")

		#TitleBar(self.centralwidget,self.gridLayout,'CRMaster9000',font,main_window)

		self.main_frame = QtWidgets.QFrame(self.centralwidget)
		self.main_frame.setStyleSheet("background-color: rgb(44, 44, 44);")
		self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.main_frame.setObjectName("main_frame")

		self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
		self.verticalLayout.setObjectName("verticalLayout")

		#Top buttons
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.top_button_box = QtWidgets.QGroupBox(self.main_frame)
		self.top_button_box.setEnabled(True)
		self.top_button_box.setMinimumSize(QtCore.QSize(0, 35))
		self.top_button_box.setMaximumSize(QtCore.QSize(175, 16777215))
		self.top_button_box.setAutoFillBackground(False)
		self.top_button_box.setStyleSheet("border-color: rgb(0, 0, 0);\n""gridline-color: rgb(0, 0, 0);")
		self.top_button_box.setObjectName("top_button_box")
		self.gridLayout_3 = QtWidgets.QGridLayout(self.top_button_box)
		self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
		self.gridLayout_3.setObjectName("gridLayout_3")
		#abrir button
		self.abrir_button = QtWidgets.QPushButton('Abrir',self.top_button_box,
			clicked=lambda:MainWindowCommands.abrir(self.direction_label,self.table))
		self.abrir_button.setFont(qtg.QFont(font[0],font[1]))
		self.abrir_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.517364, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n""color: rgb(255, 255, 255);")
		self.abrir_button.setObjectName("abrir_button")
		self.gridLayout_3.addWidget(self.abrir_button, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
		#crear button
		self.crear_button = QtWidgets.QPushButton('Crear',self.top_button_box,
			clicked=lambda:self.show_crear(MainWindowCommands,self.direction_label,self.table))
		self.crear_button.setFont(qtg.QFont(font[0],font[1]))
		self.crear_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.517364, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n""color: rgb(255, 255, 255);")
		self.crear_button.setAutoDefault(False)
		self.crear_button.setFlat(False)
		self.crear_button.setObjectName("crear_button")
		self.gridLayout_3.addWidget(self.crear_button, 0, 0, 1, 1)

		self.horizontalLayout_3.addWidget(self.top_button_box)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_3.addItem(spacerItem)
		#combobox
		self.combo_box = QtWidgets.QComboBox(self.main_frame)
		self.combo_box.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.517364, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n"
"color: rgb(255, 255, 255);")
		self.combo_box.setObjectName("combo_box")
		self.combo_box.addItem("oid")
		self.combo_box.addItem("Nombre")
		self.combo_box.addItem("Apellido")
		self.combo_box.addItem("Telefono")
		self.combo_box.addItem("DNI")
		self.combo_box.addItem("Email")
		self.horizontalLayout_3.addWidget(self.combo_box)
		#filter entry
		self.buscar_entry = QtWidgets.QLineEdit(self.main_frame)
		self.buscar_entry.setStyleSheet("color: rgb(255, 255, 255);")
		self.buscar_entry.setMaximumSize(QtCore.QSize(150, 16777215))
		self.buscar_entry.setObjectName("buscar_entry")
		self.horizontalLayout_3.addWidget(self.buscar_entry)
		#filter button
		self.buscar_button = QtWidgets.QPushButton('Buscar',self.main_frame,
			clicked=lambda:MainWindowCommands.filter(self.buscar_entry.text(),entry_tuple,self.table,self.combo_box.currentText()))
		self.buscar_button.setFont(qtg.QFont(font[0],font[1]))
		self.buscar_button.setMaximumSize(QtCore.QSize(50, 16777215))
		self.buscar_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.517364, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n""color: rgb(255, 255, 255);")
		self.buscar_button.setObjectName("buscar_button")
		self.horizontalLayout_3.addWidget(self.buscar_button)

		self.verticalLayout.addLayout(self.horizontalLayout_3)

		#direction label
		self.direction_label = QtWidgets.QLabel(self.main_frame)
		self.direction_label.setStyleSheet("color: rgb(255, 255, 255);")
		self.direction_label.setFont(qtg.QFont(font[0],font[1]))
		self.direction_label.setText("")
		self.direction_label.setObjectName("direction_label")
		self.verticalLayout.addWidget(self.direction_label)

		#table
		self.table = QtWidgets.QTableWidget(self.main_frame)
		self.table.setMinimumSize(QtCore.QSize(605, 300))
		self.table.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(21, 21, 21, 255), stop:1 rgba(62, 62, 62, 255));\n""color: rgb(255, 255, 255);")
		style = "::section {""background-color:rgb(44, 44, 44); }"
		self.table.horizontalHeader().setStyleSheet(style)
		self.table.setObjectName("table")
		self.table.horizontalHeader().setDefaultSectionSize(1)
		self.table.horizontalHeader().setSortIndicatorShown(True)
		self.table.horizontalHeader().setStretchLastSection(True)
		self.table.resizeColumnsToContents()
		self.table.verticalHeader().setVisible(False)
		self.table.verticalHeader().setDefaultSectionSize(1)
		self.table.setColumnCount(6)
		#headers
		self.table.setHorizontalHeaderLabels(['oid','Nombre','Apellido','Telefono','DNI','Email'])
		#column widths
		self.table.setColumnWidth(0,20)
		self.table.setColumnWidth(1,110)
		self.table.setColumnWidth(2,110)
		self.table.setColumnWidth(3,110)
		self.table.setColumnWidth(4,110)
		self.table.setColumnWidth(5,110)
		self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

		self.verticalLayout.addWidget(self.table)

		#entry layout
		self.entry_box = QtWidgets.QGroupBox(self.main_frame)
		self.entry_box.setMinimumSize(QtCore.QSize(600, 60))
		self.entry_box.setObjectName("entry_box")
		#grid
		self.gridLayout_2 = QtWidgets.QGridLayout(self.entry_box)
		self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
		self.gridLayout_2.setHorizontalSpacing(6)
		self.gridLayout_2.setObjectName("gridLayout_2")
		#labels
		#nombre
		self.nombre_label = QtWidgets.QLabel('Nombre',self.entry_box)
		self.nombre_label.setFont(qtg.QFont(font[0],font[1]))
		self.nombre_label.setStyleSheet("color: rgb(255, 255, 255);")
		self.nombre_label.setObjectName("nombre_label")
		self.gridLayout_2.addWidget(self.nombre_label, 0, 0, 1, 1)
		#apellido
		self.apellido_label = QtWidgets.QLabel('Apellido',self.entry_box)
		self.apellido_label.setFont(qtg.QFont(font[0],font[1]))
		self.apellido_label.setStyleSheet("color: rgb(255, 255, 255);")
		self.apellido_label.setObjectName("apellido_label")
		self.gridLayout_2.addWidget(self.apellido_label, 1, 0, 1, 1)
		#telefono
		self.telefono_label = QtWidgets.QLabel('Telefono',self.entry_box)
		self.telefono_label.setFont(qtg.QFont(font[0],font[1]))
		self.telefono_label.setStyleSheet("color: rgb(255, 255, 255);")
		self.telefono_label.setObjectName("telefono_label")
		self.gridLayout_2.addWidget(self.telefono_label, 0, 2, 1, 1)
		#dni
		self.dni_label = QtWidgets.QLabel('DNI',self.entry_box)
		self.dni_label.setFont(qtg.QFont(font[0],font[1]))
		self.dni_label.setStyleSheet("color: rgb(255, 255, 255);")
		self.dni_label.setObjectName("dni_label")
		self.gridLayout_2.addWidget(self.dni_label, 1, 2, 1, 1)
		#email
		self.email_label = QtWidgets.QLabel('Email',self.entry_box)
		self.email_label.setFont(qtg.QFont(font[0],font[1]))
		self.email_label.setStyleSheet("color: rgb(255, 255, 255);")
		self.email_label.setObjectName("email_label")
		self.gridLayout_2.addWidget(self.email_label, 0, 4, 1, 1)
		#oid
		self.oid_label = QtWidgets.QLabel('oid',self.entry_box)
		self.oid_label.setFont(qtg.QFont(font[0],font[1]))
		self.oid_label.setStyleSheet("color: rgb(255, 255, 255);")
		self.oid_label.setObjectName("oid_label")
		self.gridLayout_2.addWidget(self.oid_label, 1, 4, 1, 1)
		#entries
		#nombre
		self.nombre_entry = QtWidgets.QLineEdit(self.entry_box)
		self.nombre_entry.setStyleSheet("color: rgb(255, 255, 255);")
		self.nombre_entry.setObjectName("nombre_entry")
		self.gridLayout_2.addWidget(self.nombre_entry, 0, 1, 1, 1)
		#apellido
		self.apellido_entry = QtWidgets.QLineEdit(self.entry_box)
		self.apellido_entry.setStyleSheet("color: rgb(255, 255, 255);")
		self.apellido_entry.setObjectName("apellido_entry")
		self.gridLayout_2.addWidget(self.apellido_entry, 1, 1, 1, 1)
		#telefono
		self.telefono_entry = QtWidgets.QLineEdit(self.entry_box)
		self.telefono_entry.setStyleSheet("color: rgb(255, 255, 255);")
		self.telefono_entry.setObjectName("telefono_entry")
		self.gridLayout_2.addWidget(self.telefono_entry, 0, 3, 1, 1)
		#dni
		self.dni_entry = QtWidgets.QLineEdit(self.entry_box)
		self.dni_entry.setStyleSheet("color: rgb(255, 255, 255);")
		self.dni_entry.setObjectName("dni_entry")
		self.gridLayout_2.addWidget(self.dni_entry, 1, 3, 1, 1)
		#email
		self.email_entry = QtWidgets.QLineEdit(self.entry_box)
		self.email_entry.setStyleSheet("color: rgb(255, 255, 255);")
		self.email_entry.setObjectName("email_entry")
		self.gridLayout_2.addWidget(self.email_entry, 0, 5, 1, 1)
		#oid
		self.oid_entry = QtWidgets.QLineEdit(self.entry_box)
		self.oid_entry.setReadOnly(True)
		self.oid_entry.setStyleSheet("color: rgb(255, 255, 255);")
		self.oid_entry.setObjectName("oid_entry")
		self.gridLayout_2.addWidget(self.oid_entry, 1, 5, 1, 1)
		self.verticalLayout.addWidget(self.entry_box)#place the entry_box in the main layout

		entry_tuple=(self.nombre_entry,self.apellido_entry,self.telefono_entry,self.dni_entry,self.email_entry,self.oid_entry)

		#bottom buttons
		self.bottom_button_layout = QtWidgets.QHBoxLayout()
		self.bottom_button_layout.setObjectName("bottom_button_layout")
		#cargar button
		self.cargar_button = QtWidgets.QPushButton('Cargar',self.main_frame,
			clicked=lambda:MainWindowCommands.cargar(entry_tuple,self.table))
		self.cargar_button.setFont(qtg.QFont(font[0],font[1]))
		self.cargar_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.517364, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n""color: rgb(255, 255, 255);")
		self.cargar_button.setObjectName("cargar_button")
		self.bottom_button_layout.addWidget(self.cargar_button)
		#borrar button
		self.borrar_button = QtWidgets.QPushButton('Borrar',self.main_frame,
			clicked=lambda:MainWindowCommands.borrar(self.table,entry_tuple))
		self.borrar_button.setFont(qtg.QFont(font[0],font[1]))
		self.borrar_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.517364, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n""color: rgb(255, 255, 255);")
		self.borrar_button.setObjectName("borrar_button")
		self.bottom_button_layout.addWidget(self.borrar_button)
		#modificar button
		self.modificar_button = QtWidgets.QPushButton('Modificar',self.main_frame,
			clicked=lambda:MainWindowCommands.modificar(entry_tuple,self.table))
		self.modificar_button.setFont(qtg.QFont(font[0],font[1]))
		self.modificar_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.517364, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n""color: rgb(255, 255, 255);")
		self.modificar_button.setObjectName("modificar_button")
		self.bottom_button_layout.addWidget(self.modificar_button)
		#limpiar button
		self.limpiar_button = QtWidgets.QPushButton('Limpiar entries',self.main_frame,
			clicked=lambda:MainWindowWidgets.reset_entries(entry_tuple))
		self.limpiar_button.setFont(qtg.QFont(font[0],font[1]))
		self.limpiar_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.517364, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n""color: rgb(255, 255, 255);")
		self.limpiar_button.setObjectName("limpiar_button")
		self.bottom_button_layout.addWidget(self.limpiar_button)
		#log button
		self.log_button = QtWidgets.QPushButton('Ver log',self.main_frame,
			clicked=lambda:self.show_log(MainWindowCommands))
		self.log_button.setFont(qtg.QFont(font[0],font[1]))
		self.log_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.517364, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n""color: rgb(255, 255, 255);")
		self.log_button.setObjectName("log_button")
		self.bottom_button_layout.addWidget(self.log_button)
		#aux button
		self.aux_button = QtWidgets.QPushButton('Panic Button!',self.main_frame,
			clicked=lambda:MainWindowCommands.aux())
		self.aux_button.setFont(qtg.QFont(font[0],font[1]))
		self.aux_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.517364, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n""color: rgb(255, 255, 255);")
		self.aux_button.setObjectName("aux_button")
		self.bottom_button_layout.addWidget(self.aux_button)

		self.verticalLayout.addLayout(self.bottom_button_layout)

		self.gridLayout.addWidget(self.main_frame, 1, 0, 1, 1)

		main_window.setCentralWidget(self.centralwidget)
		#bindings
		self.table.doubleClicked.connect(lambda:MainWindowCommands.seleccionar(self,entry_tuple,self.table))
		for entry in entry_tuple:
			entry.returnPressed.connect(lambda:MainWindowCommands.cargar(entry_tuple,self.table))
		self.table.horizontalHeader().sectionClicked.connect(lambda index:MainWindowCommands.sort(index,self.table))

	def update_label(label,new_text):
		'''cambia el texto en el label indicado'''
		label.setText(new_text)

	def reset_entries(entry_tuple):
		'''borra el texto en las entries'''
		for entry in entry_tuple:
			entry.setText('')

	def update_table(table,datos):
		'''carga los datos en la tabla resibida'''
		table.setRowCount(0)
		for dato in datos:
			numRows = table.rowCount()
			table.insertRow(numRows)
			x=0
			for d in dato:
				table.setItem(numRows,x,QtWidgets.QTableWidgetItem(str(dato[x])))
				x+=1

	def cargar_datos(entry_tuple,datos):
		'''carga los datos en las entries'''
		contador=0
		for entry in entry_tuple:
			entry.setText(str(datos[contador]))
			contador+=1

	def show_crear(self,MainWindowCommands,direction_label,table):
		'''Abre la ventana de crear database'''
		self.crear_window = QtWidgets.QWidget()
		ui=TopLevelCrear()
		ui.setupUi(self.crear_window,MainWindowCommands,direction_label,table)
		self.crear_window.show()

	def show_log(self,MainWindowCommands):
		'''Abre la ventana del registro'''
		self.log_window = QtWidgets.QWidget()
		ui = TopLevelLog()
		log_tree=ui.setupUi(self.log_window)
		self.log_window.show()
		MainWindowCommands.cargar_log(log_tree)