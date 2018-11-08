# coding: utf-8
import csv
import math
from sklearn.tree import export_graphviz
import graphviz


class ID3(object):

#carga el fichero como .csv
    def __init__(self, fichero):
        self.fichero = fichero
        Ninst = len(open(fichero).readlines())-1
        print("Esto tiene:",Ninst,"instancias")
		lector = csv.DictReader(open(fichero))
		self.lector = lector

    def clasifica(self, instancia):
        self.instancia = instancia
        #Devuelve clase, con la clase predicha
        pass
        
        
    def test(self, fichero):
            aciertos = 0
            total = 0
            test = parseData(sys.argv[2], int(sys.argv[3]))
            for avanzarconalegria in test:
                claseP = evalua(arbol, avanzarconalegria)
                total += 1
                if claseP == avanzarconalegria[1]:
                    aciertos += 1
        tasa = aciertos/total
        pass


    def save_tree(self, fichero):
    	export_graphviz(clasificadorArbol, out_file='railway.dot',class_names=fichero.target_names,feature_names=fichero.feature_names,impurity=False,filled=True)
    	with open('railway.dot') as f:
    		dot_grap=f.read()
    	graphviz.Source(dot_grap).view()
        
#id3 = ID3('railway.train')
#clase = id3.clasifica({'season':'winter','rain':'heavy','wind':'high','day':'saturday'})
#print('Clase:',clase)
#(aciertos,total,tasa) = id3.test('railway.test')
#print('Aciertos:',aciertos,'Total:',total,'Tasa:',tasa)

id3 = ID3('railway.data')
id3.save_tree('railway.dot')
