# coding: utf-8
import csv

class ID3(object):

    def __init__(self, fichero):
		self.fichero = fichero
		with open(fichero) as cvsfile:
			lector = csv.reader(cvsfile, delimiter=',')
			#linea = 0
			for row in lector:
				#if linea == 0:
					print(', '.join(row))
					#else:
	     #			print(', '.join(row))
	     #			linea += 1
id3 = ID3('railway.data')
