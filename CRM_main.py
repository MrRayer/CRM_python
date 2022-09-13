from CRM_view import *
from CRM_model import *
from CRM_filter import filtrar
import re,sys

#Author Céspedes Rodrigo
#Finish date: 16/2/22

#regex list name
OID_CHECK='[0-9]{1,2}'
CREAR_CHECK='[a-zA-Z0-9_ ]'

def dir_check(funcion):
	'''Este decorador hace un check a la direccion para asegurarse de que haya una cargada'''
	def wrapper(*args,**kwargs):
		global direccion
		if direccion != '':
			funcion(*args,**kwargs)
		else:
			load_error()
	return wrapper

class MainWindowCommands():
	''' clase que contiene los comandos utilizados por los botones de la ventana principal '''
	def crear(self,data_base_name,direction_label,tree,crear_db):
		'''crea una database en la direccion indicada y con el nombre indicado,
		luego crea una sesion con esta y carga los tados de la Lista'''
		crear_db.destroy()
		global direccion
		if(re.search(CREAR_CHECK,data_base_name)):
			direccion=QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
			direccion=f'{direccion}/{data_base_name}.db'
			MainWindowWidgets.update_label(direction_label,direccion)
			self.destroy()
			DataBase.crear(direccion)
			MainWindowWidgets.update_label(direction_label,direccion)
			DataBase.abrir(direccion)
			print(f'Base de datos creada en : {direccion}')
			datos=DataBase.mostrar()
			MainWindowWidgets.update_table(tree,datos)
		else:
			custom_error('Error','Nombre invalido')

	def abrir(direction_label,treeview):
		'''guarda la direccion de la database a utilizar en la variable global direccion'''
		global direccion
		old_dir=direccion
		direccion_t=QtWidgets.QFileDialog.getOpenFileName(filter="*.db")
		direccion=direccion_t[0]
		if direccion == '':
			direccion=old_dir
			return
		MainWindowWidgets.update_label(direction_label,direccion)
		DataBase.abrir(direccion)
		print(f'direccion cargada: {direccion}')
		datos=DataBase.mostrar()
		MainWindowWidgets.update_table(treeview,datos)

	@dir_check
	def cargar(entry_tuple,treeview):
		'''recibe los datos de la entry tuple, los carga en la database y recarga el qtablewidget'''
		respuesta=filtrar(entry_tuple)
		if respuesta == True:
			dni_list=DataBase.dni_list()
			flag=True
			for dni in dni_list:
				if str(dni)==entry_tuple[3].text():
					flag=False
			if flag==True:
				datos=(entry_tuple[0].text(),entry_tuple[1].text(),entry_tuple[2].text(),entry_tuple[3].text(),entry_tuple[4].text())
				datos=DataBase.cargar(datos)
				datos=DataBase.mostrar()
				MainWindowWidgets.update_table(treeview,datos)
				MainWindowWidgets.reset_entries(entry_tuple)
				print(f'datos cargados en database {direccion}')
			else:
				custom_error('Load error','Error cargando los datos en la DB, posiblemente el DNI ya exista en la base')

	@dir_check
	def borrar(treeview,entry_tuple):
		'''Toma la columna en focus, se la envia al model para borrar y recarga el qtablewidget'''
		seleccion=treeview.currentRow()
		if seleccion != -1:
			oid=treeview.item(seleccion,0).text()
			r=QtWidgets.QMessageBox.question(None,'', f"Borrar datos en la id {oid}", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
			if r == QtWidgets.QMessageBox.Yes:
				DataBase.borrar(oid)
				print(f'datos borrados en oid {oid} direccion {direccion}')
				datos=DataBase.mostrar()
				MainWindowWidgets.update_table(treeview,datos)
				MainWindowWidgets.reset_entries(entry_tuple)

	@dir_check
	def modificar(entry_tuple,treeview):
		'''Toma la id de las entries, hacer un check con la database para asegurarse de que exista en esta,
		modifica los datos existentes en dicha id con los de las entries y recarga el qtablewidget'''
		flag=0
		ids=DataBase.id_list()
		seleccion=entry_tuple[5].text()
		try:
			for id in ids:
				if int(id)==int(seleccion):
					flag=1
		except:
			pass
		if flag==1:
			respuesta=filtrar(entry_tuple)
			if respuesta == True:
				datos=(entry_tuple[0].text(),entry_tuple[1].text(),entry_tuple[2].text(),entry_tuple[3].text(),entry_tuple[4].text(),entry_tuple[5].text())
				DataBase.update(datos)
				MainWindowWidgets.reset_entries(entry_tuple)
				print(f'datos modificados en oid {datos[5]} direccion {direccion}')
				datos=DataBase.mostrar()
				MainWindowWidgets.update_table(treeview,datos)
				flag=0
		else:
			custom_error('OID error','Oid invalida')

	@dir_check
	def cargar_log(tree):
		'''Setea un observer para recargar el registro cuando este cambia'''
		obs1=Observer(MainWindowCommands,tree)
		datos=DataBase.load_log()
		MainWindowWidgets.update_table(tree,datos)

	def update_log(tree):
		'''Recarga el registro a pedido del oberver'''
		datos=DataBase.load_log()
		MainWindowWidgets.update_table(tree,datos)

	@dir_check
	def seleccionar(self,entry_tuple,treeview):
		'''Al hacer doble click carga los datos seleccionados en las entries'''
		seleccion=treeview.currentRow()
		sid=treeview.item(seleccion,0).text()
		datos=DataBase.query_id(sid)
		MainWindowWidgets.reset_entries(entry_tuple)
		MainWindowWidgets.cargar_datos(entry_tuple,datos)

	@dir_check
	def sort(index,table):
		'''Al hacer click en un header de la qtablewidget ordena los elementos de este en orden alfabetico'''
		datos=DataBase.mostrar(index)
		MainWindowWidgets.update_table(table,datos)

	@dir_check
	def filter(filter_str,entry_tuple,table,cb):
		'''Filtra los resultados del query en la database dependiendo de lo seleccionado'''
		datos=DataBase.mostrar_f(filter_str,cb)
		MainWindowWidgets.update_table(table,datos)

	def aux():
		'''ignorar, usado para testear y me termino gustando'''
		custom_error(':O','Hello World!')

if __name__ == '__main__':
	''' en caso de haber sido abierto y no importado, inicia la app '''
	direccion=''
	app = QtWidgets.QApplication(sys.argv)
	main_window = QtWidgets.QMainWindow()
	ui = MainWindowWidgets()
	ui.setupUi(main_window,MainWindowCommands)
	main_window.show()
	sys.exit(app.exec_())
else:
	print('Este archivo no puede ser importado')
