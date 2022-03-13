#Universidad del Valle de Guatemala
#Inteligencia Artificial
#Integrantes:
# Bryann Alfaro
# Raul Jimenez
# Donaldo Garcia
# Oscar Saravia

import math
import sys


ciudad_inicial = sys.argv[1]
ciudades = sys.argv[2]

def distance_points(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


#Abrir archivo de definicion de ciudades
ciudades = open(ciudades, "r")
numero_ciudades = ciudades.readline()

print(numero_ciudades)

ciudades_list = {}
indice = 1
for ciudad in ciudades:
    ciudades_list['ciudad '+str(indice)] = {'x':int(ciudad.split()[0]), 'y':int(ciudad.split()[1])}
    indice+=1
#print(distance_points())
print(ciudades_list)
