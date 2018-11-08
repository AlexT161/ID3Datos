# coding: utf-8
import csv

class ID3(object):

	def __init__(self, fichero):
		self.fichero = fichero
		Ninst = len(open(fichero).readlines())-1
		print("Esto tiene:",Ninst,"instancias")
		lector = csv.DictReader(open(fichero))
		interno = {}
		d = 0
		diccionario = {}
		for ord_dict in lector:
			for key,value in ord_dict.items():
				interno [key] = value
			diccionario[d] = interno
			d += 1
		print(diccionario.keys())
		print(diccionario)

id3 = ID3('railway.data')