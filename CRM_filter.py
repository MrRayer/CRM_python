import re
from CRM_view import custom_error

#regex entries
NOMBRE_CHECK='^\D[A-Za-z]*\D$'
APELLIDO_CHECK='^\D[A-Za-z]*\D$'
TELEFONO_CHECK='^\w[0-9]{5,11}\w$'
DNI_CHECK='^[0-9]{8}$'
EMAIL_CHECK='[A-Za-z0-9\.\-\_]+@(gmail|hotmail)+\.(com)\.?(ar)?'

def filtrar(entry_tuple):
	'''Filtra la entry tuple y comprueba la longitud de ciertos strings'''
	if(re.search(NOMBRE_CHECK,entry_tuple[0].text())) and (re.search(APELLIDO_CHECK,entry_tuple[1].text())) and (re.search(TELEFONO_CHECK,entry_tuple[2].text())) and (re.search(DNI_CHECK,entry_tuple[3].text())) and (re.search(EMAIL_CHECK,entry_tuple[4].text())):
		if len(entry_tuple[0].text()) <= 20 and len(entry_tuple[1].text()) <= 20 and len(entry_tuple[4].text()) <= 40:
			return True
		else:
			if not len(entry_tuple[0].text()) <= 20:
				custom_error('Nombre invalido','Nombre muy largo, max 20 caracteres')
			elif not len(entry_tuple[1].text()) <= 20:
				custom_error('Apellido invalido','Nombre muy largo, max 20 caracteres')
			elif not len(entry_tuple[4].text()) <= 40:
				custom_error('Email invalido','Nombre muy largo, max 40 caracteres')
			return False
	else:
		if not(re.search(NOMBRE_CHECK,entry_tuple[0].text())):
			custom_error('Nombre invalido','Nombre invalido, solo letras')
		elif not(re.search(APELLIDO_CHECK,entry_tuple[1].text())):
			custom_error('Apellido invalido','Apellido invalido, solo letras')
		elif not(re.search(TELEFONO_CHECK,entry_tuple[2].text())):
			custom_error('Telefono invalido','Telefono invalido, solo entre 8 y 12 numeros')
		elif not(re.search(DNI_CHECK,entry_tuple[3].text())):
			custom_error('DNI invalido','DNI invalido, solo 8 numeros')
		elif not(re.search(EMAIL_CHECK,entry_tuple[4].text())):
			custom_error('Email invalido','Email invalido, formato: xxx@xxx.com')
		return False