import sqlite3, datetime, time
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == '__main__':
	print('open from CRM_main.py')

def log_action(funcion):
	'''Decorador que carga informacion de las acciones realizadas a la tabla principal'''
	def wrapper(*args,**kwargs):
		global session
		dato=funcion(*args,**kwargs)
		date=datetime.datetime.now().strftime("%Y-%m-%d")
		time=datetime.datetime.now().strftime("%H:%M:%S")
		if funcion.__name__ == 'cargar':
			ida='NEW ENTRY'
		elif funcion.__name__ == 'update':
			datos=args[0]
			ida=datos[5]
		elif funcion.__name__ == 'borrar':
			oid=args[0]
			ida=oid
		new_entry_log=Log(Accion=funcion.__name__,
					  Ida=ida,
					  Fecha=date,
					  Hora=time)
		session.add(new_entry_log)
		session.commit()
		Observer.notif()
		return dato
	return wrapper

Base=declarative_base()
class Lista(Base):
	'''Modelo de la tabla principal dentro de la base de datos'''
	__tablename__='lista'
	id=Column(Integer(),primary_key=True)
	Nombre=Column(String(20),nullable=False,unique=False)
	Apellido=Column(String(20),nullable=False,unique=False)
	Telefono=Column(Integer(),nullable=True,unique=False)
	DNI=Column(Integer(),nullable=False,unique=True)
	Email=Column(String(40),nullable=True,unique=False)

class Log(Base):
	'''Modelo de la tabla log dentro de la base de datos'''
	__tablename__='log'
	id=Column(Integer(),primary_key=True)
	Accion=Column(String(),nullable=False,unique=False)
	Ida=Column(Integer(),nullable=True,unique=False)
	Fecha=Column(String(),nullable=False,unique=False)
	Hora=Column(String(),nullable=False,unique=False)

class Observer():
	'''Observer que recarga el registro cuando nueva info se le agrega'''
	com=None
	log=None
	def __init__(self,MainWindowCommands,tree):
		Observer.com=MainWindowCommands
		Observer.log=tree
	def notif():
		try:
			Observer.com.update_log(Observer.log)
		except:
			pass

class DataBase():
	'''Clase principal del model'''
	def crear(direccion):
		'''Crea el engine en la direccion especificada'''
		engine=DataBase.abrir(direccion)
		Base.metadata.create_all(engine)

	def abrir(direccion):
		'''crea la session a la database en la direccion especificada'''
		global session
		direccion='sqlite:///'+direccion
		engine=create_engine(direccion,echo=False)
		Session=sessionmaker(bind=engine)
		session=Session()
		print('Session creada')
		return engine

	def aux():
		'''ignorar'''
		return (':O','HELLO WORLD!')

	@log_action
	def cargar(datos):
		'''carga los datos en la database'''
		global session
		new_entry=Lista(Nombre=datos[0],
						Apellido=datos[1],
						Telefono=datos[2],
						DNI=datos[3],
						Email=datos[4])
		session.add(new_entry)
		session.commit()

	@log_action
	def update(datos):
		'''reemplaza los datos en la database'''
		global session
		new=session.query(Lista).filter(Lista.id==datos[5]).first()
		new.Nombre=datos[0]
		new.Apellido=datos[1]
		new.Telefono=datos[2]
		new.DNI=datos[3]
		new.Email=datos[4]
		session.commit()

	def query_id(sid):
		'''Devuelve la info guardada en la id'''
		global session
		q=session.query(Lista).filter(Lista.id==sid).first()
		datos=(q.Nombre,q.Apellido,q.Telefono,q.DNI,q.Email,sid)
		return datos

	def mostrar(index=0):
		'''Devuelve la Lista en orden alfabetico'''
		global session
		if index==0:
			lista=session.query(Lista).order_by(Lista.id)
		elif index==1:
			lista=session.query(Lista).order_by(Lista.Nombre)
		elif index==2:
			lista=session.query(Lista).order_by(Lista.Apellido)
		elif index==3:
			lista=session.query(Lista).order_by(Lista.Telefono)
		elif index==4:
			lista=session.query(Lista).order_by(Lista.DNI)
		elif index==5:
			lista=session.query(Lista).order_by(Lista.Email)
		datos=[]
		for x in lista:
			y=(x.id,x.Nombre,x.Apellido,x.Telefono,x.DNI,x.Email)
			datos.append(y)
		return datos

	def mostrar_f(filter_str,cb):
		'''Devuelve los resultados que coincidan con el filtro'''
		global session
		if filter_str != '':
			search = f'%{filter_str}%'
			if cb=='oid':
				lista=session.query(Lista).filter(Lista.id.like(search)).all()
			if cb=='Nombre':
				lista=session.query(Lista).filter(Lista.Nombre.like(search)).all()
			if cb=='Apellido':
				lista=session.query(Lista).filter(Lista.Apellido.like(search)).all()
			if cb=='Telefono':
				lista=session.query(Lista).filter(Lista.Telefono.like(search)).all()
			if cb=='DNI':
				lista=session.query(Lista).filter(Lista.DNI.like(search)).all()
			if cb=='Email':
				lista=session.query(Lista).filter(Lista.Email.like(search)).all()
		elif filter_str == '':
			lista=session.query(Lista).order_by(Lista.id)
		datos=[]
		for x in lista:
			y=(x.id,x.Nombre,x.Apellido,x.Telefono,x.DNI,x.Email)
			datos.append(y)
		return datos


	def id_list():
		'''Devuelve una lista de ids'''
		global session
		lista=session.query(Lista).all()
		datos=[]
		for x in lista:
			datos.append(x.id)
		return datos

	def dni_list():
		'''Devuelve una lista de DNIs'''
		global session
		lista=session.query(Lista).all()
		datos=[]
		for x in lista:
			datos.append(x.DNI)
		return datos

	@log_action
	def borrar(ids):
		'''Borra los datos en la id seleccionada'''
		global session
		new=session.query(Lista).filter(Lista.id==ids).first()
		session.delete(new)
		session.commit()

	def load_log():
		'''Devuelve los datos del registro'''
		global session
		log=session.query(Log).all()
		datos=[]
		for x in log:
			y=(x.id,x.Accion,x.Ida,x.Fecha,x.Hora)
			datos.append(y)
		return datos