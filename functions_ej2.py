import math
import numpy as np


def distance_points(a, b):
    return math.sqrt((a['x']-b['x'])**2 + (a['y']-b['y'])**2)


def total_distance(ciudades_list):
    total = 0
    longitud = len(ciudades_list)
    for i in range(len(ciudades_list)):
        try:
            total += distance_points(
                ciudades_list[f'ciudad {str(i+1)}'],
                ciudades_list[f'ciudad {str(i + 2)}'],
            )

        except:
            pass

    total += distance_points(ciudades_list['ciudad 1'],
                             ciudades_list['ciudad '+str(longitud).rstrip("\n")])
    return total


def sim_annealing(ciudades_list, numero_ciudades, ciudad_inicial):
    before = ciudades_list.copy()
    cost0 = total_distance(ciudades_list)
    T = 30
    factor = 0.99
    T_init = T
    costo = 0
    for _ in range(1000):
        T = T * factor
        for j in range(500):
            r1, r2 = np.random.randint(0, numero_ciudades, size=2)
            r1 = r1+1
            r2 = r2+1
            temp = ciudades_list[f'ciudad {str(r1)}']
            ciudades_list[f'ciudad {str(r1)}'] = ciudades_list[f'ciudad {str(r2)}']
            ciudades_list[f'ciudad {str(r2)}'] = temp
            cost1 = total_distance(ciudades_list)

            if cost1 < cost0:
                cost0 = cost1
            else:
                x = np.random.uniform()
                if x < np.exp((cost0-cost1)/T):
                    cost0 = cost1
                else:
                    temp = ciudades_list[f'ciudad {str(r1)}']
                    ciudades_list['ciudad ' +
                                  str(r1)] = ciudades_list[f'ciudad {str(r2)}']
                    ciudades_list[f'ciudad {str(r2)}'] = temp
    costo = cost0
    after = ciudades_list
    recorrido = []

    for i in range(len(list(ciudades_list))):
        if after['ciudad '+str(i+1)] == ciudad_inicial:
            for key, value in before.items():
                if value == after['ciudad '+str(i+1)]:
                    recorrido.append(key)
            i = i+1
            for j in range(len(list(ciudades_list))):

                j = j+1
                if (i+j) % len(list(ciudades_list)) == 0:
                    for key, value in before.items():
                        if value == after['ciudad '+str(len(list(ciudades_list)))]:
                            recorrido.append(key)
                else:
                    for key, value in before.items():
                        if value == after['ciudad '+str((i+j) % len(list(ciudades_list)))]:
                            recorrido.append(key)
    return costo, ciudades_list, recorrido
