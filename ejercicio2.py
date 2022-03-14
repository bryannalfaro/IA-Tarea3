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
from matplotlib import pyplot as plt

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

f = 'ciudad ' +str(numero_ciudades)
fig = plt.figure()
#ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
#print(list(ciudades_list))
#for first, second in zip(list(ciudades_list)[:-1],list(ciudades_list)[1:]):
#    ax1.plot([ciudades_list[first]['x'], ciudades_list[second]['x']], [ciudades_list[first]['y'], ciudades_list[second]['y']], '-o')
#ax1.plot([(ciudades_list)['ciudad 1']['x'], (ciudades_list)[f.rstrip("\n")]['x']], [(ciudades_list)['ciudad 1']['y'], ciudades_list[f.rstrip("\n")]['y']], '-o')

#for c in list(ciudades_list):
#    ax1.plot(ciudades_list[c]['x'], ciudades_list[c]['y'], 'bo')

recorrido = []
#print('Ciudades: ',ciudades_list)
costo,ciudades_list,recorrido=sim_annealing(ciudades_list,numero_ciudades,ciudad_inicial)
#print('AFTER',ciudades_list)
for first, second in zip(list(ciudades_list)[:-1],list(ciudades_list)[1:]):
    #print(first,second)
    ax2.plot([ciudades_list[first]['x'], ciudades_list[second]['x']], [ciudades_list[first]['y'], ciudades_list[second]['y']], '-o')
ax2.plot([(ciudades_list)['ciudad 1']['x'], (ciudades_list)[f.rstrip("\n")]['x']], [(ciudades_list)['ciudad 1']['y'], ciudades_list[f.rstrip("\n")]['y']], '-o')

for c in list(ciudades_list):
    ax2.plot(ciudades_list[c]['x'], ciudades_list[c]['y'], 'bo')

print('Distancia optimizada final: ',costo)
print(recorrido)
plt.show()