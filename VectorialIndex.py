# Insertar aqui la cabecera

import string

# Dada una linea de texto, devuelve una lista de palabras no vacias 
# convirtiendo a minusculas y eliminando signos de puntuacion por los extremos
# Ejemplo:
#   > extrae_palabras("Hi! What is your name? John.")
#   ['hi', 'what', 'is', 'your', 'name', 'john']
def extrae_palabras(linea):
  return filter(lambda x: len(x) > 0, 
    map(lambda x: x.lower().strip(string.punctuation), linea.split()))


class VectorialIndex(object):

    def __init__(self, directorio, stop=[]):
        pass

    def consulta_vectorial(self, consulta, n=3):
        pass

    def consulta_conjuncion(self, consulta):
        pass
