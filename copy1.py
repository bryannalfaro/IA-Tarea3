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
import random
import numpy as np
ciudad_inicial = sys.argv[1]
ciudades = sys.argv[2]


#Abrir archivo de definicion de ciudades
ciudades = open(ciudades, "r")
numero_ciudades = ciudades.readline()

#print('Numero de ciudades: \n',numero_ciudades)

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

'''print('Ciudad inicial: ',num_ciudad_inicial,' con coordenadas: ',ciudad_inicial)

print('Lista de ciudades \n',ciudades_list)

print('Distancia total: ', total_distance(ciudades_list))'''
f = 'ciudad ' +str(numero_ciudades)
print('sfdl;ka',ciudades_list['ciudad '+str(numero_ciudades).rstrip('\n')])
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
print(list(ciudades_list))
for first, second in zip(list(ciudades_list)[:-1],list(ciudades_list)[1:]):
    print(first,second)
    ax1.plot([ciudades_list[first]['x'], ciudades_list[second]['x']], [ciudades_list[first]['y'], ciudades_list[second]['y']], '-o')
ax1.plot([(ciudades_list)['ciudad 1']['x'], (ciudades_list)[f.rstrip("\n")]['x']], [(ciudades_list)['ciudad 1']['y'], ciudades_list[f.rstrip("\n")]['y']], '-o')

for c in list(ciudades_list):
    ax1.plot(ciudades_list[c]['x'], ciudades_list[c]['y'], 'bo')



cost0 = total_distance(ciudades_list)
T = 30
factor = 0.99
T_init = T
costo = 0
for i in range(1000):
    print(i,'cost = ',cost0)
    T = T* factor
    for j in range(500):
        r1,r2 = np.random.randint(0,numero_ciudades, size=2)
        r1 = r1+1
        r2 = r2+1
        temp = ciudades_list['ciudad '+str(r1)]
        ciudades_list['ciudad '+str(r1)] = ciudades_list['ciudad '+str(r2)]
        ciudades_list['ciudad '+str(r2)] = temp
        cost1 = total_distance(ciudades_list)

        if cost1 < cost0:
            cost0 = cost1
        else:
            x = np.random.uniform()
            if x < np.exp((cost0-cost1)/T):
                cost0 = cost1
            else:
                temp = ciudades_list['ciudad '+str(r1)]
                ciudades_list['ciudad '+str(r1)] = ciudades_list['ciudad '+str(r2)]
                ciudades_list['ciudad '+str(r2)] = temp
costo = cost0, cost1

for first, second in zip(list(ciudades_list)[:-1],list(ciudades_list)[1:]):
    print(first,second)
    ax2.plot([ciudades_list[first]['x'], ciudades_list[second]['x']], [ciudades_list[first]['y'], ciudades_list[second]['y']], '-o')
ax2.plot([(ciudades_list)['ciudad 1']['x'], (ciudades_list)[f.rstrip("\n")]['x']], [(ciudades_list)['ciudad 1']['y'], ciudades_list[f.rstrip("\n")]['y']], '-o')


print(costo)
plt.show()
