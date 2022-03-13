#Universidad del Valle de Guatemala
#Inteligencia Artificial
#Integrantes:
# Bryann Alfaro
# Raul Jimenez
# Donaldo Garcia
# Oscar Saravia


#Referencias
'''
https://realpython.com/python-dicts/
https://www.codegrepper.com/code-examples/python/how+to+find+distance+between+two+coordinates+in+python
'''
import math
import sys
from functions_ej2 import *

ciudad_inicial = sys.argv[1]
ciudades = sys.argv[2]


#Abrir archivo de definicion de ciudades
ciudades = open(ciudades, "r")
numero_ciudades = ciudades.readline()

print('Numero de ciudades: \n',numero_ciudades)

ciudades_list = {}
indice = 1
num_ciudad_inicial = ciudad_inicial
#Rellenando diccionario con ciudades y coordenadas
for ciudad in ciudades:
    ciudades_list['ciudad '+str(indice)] = {'x':int(ciudad.split()[0]), 'y':int(ciudad.split()[1])}
    try:
        if(int(ciudad_inicial) == indice):
            ciudad_inicial = ciudades_list['ciudad '+str(indice)]
    except:
        pass

    indice+=1

print('Ciudad inicial: ',num_ciudad_inicial,' con coordenadas: ',ciudad_inicial)

print('Lista de ciudades \n',ciudades_list)

print('Distancia total: ', total_distance(ciudades_list))