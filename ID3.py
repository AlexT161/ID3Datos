# coding: utf-8
import csv

class ID3(object):

    def __init__(self, fichero):
    	self.fichero = fichero
    	with open(fichero) as cvsfile:
    		fichero = csv.reader(cvsfile, delimiter=',')
	    # return lector
	    # 	linea = 0
	    # 	for row in fichero:
	    # 		if linea == 0:
	    # 			print(', '.join(row))
	    # 		else:
	    # 			print(', '.join(row))
	    # 			linea += 1
    	# Cargar archivo .csv railway.data, lens.data y car.data

    def clasifica(self, instancia):
        #for avanzarconalegria
        pass
        
        
    def test(self, fichero):
        pass


    def save_tree(self, fichero):
        pass

id3 = ID3('railway.data')
