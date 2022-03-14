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
    firstList = ciudades_list.copy()
    initialCost = total_distance(ciudades_list)
    times = 30
    factor = 0.99
    costo = 0
    for _ in range(1000):
        times *= factor
        for _ in range(500):
            r1, r2 = np.random.randint(0, numero_ciudades, size=2)
            r1 = r1+1
            r2 = r2+1
            temp = ciudades_list[f'ciudad {str(r1)}']
            ciudades_list[f'ciudad {str(r1)}'] = ciudades_list[f'ciudad {str(r2)}']
            ciudades_list[f'ciudad {str(r2)}'] = temp
            cost1 = total_distance(ciudades_list)

            if cost1 < initialCost:
                initialCost = cost1
            else:
                x = np.random.uniform()
                if x < np.exp((initialCost-cost1)/times):
                    initialCost = cost1
                else:
                    temp = ciudades_list[f'ciudad {str(r1)}']
                    ciudades_list['ciudad ' +
                                  str(r1)] = ciudades_list[f'ciudad {str(r2)}']
                    ciudades_list[f'ciudad {str(r2)}'] = temp
    costo = initialCost
    newList = ciudades_list
    recorrido = []

    for i in range(len(list(ciudades_list))):
        if newList[f'ciudad {str(i+1)}'] == ciudad_inicial:
            recorrido.extend(
                key
                for key, value in firstList.items()
                if value == newList[f'ciudad {str(i+1)}']
            )

            i = i+1
            for j in range(len(list(ciudades_list))):

                j = j+1
                if (i+j) % len(list(ciudades_list)) == 0:
                    recorrido.extend(
                        key
                        for key, value in firstList.items()
                        if value == newList[f'ciudad {len(list(ciudades_list))}']
                    )

                else:
                    recorrido.extend(
                        key
                        for key, value in firstList.items()
                        if value
                        == newList[
                            'ciudad ' + str((i + j) % len(list(ciudades_list)))
                        ]
                    )

    return costo, ciudades_list, recorrido
