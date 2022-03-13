import math

def distance_points(a,b):
    return math.sqrt((a['x']-b['x'])**2 + (a['y']-b['y'])**2)

def total_distance(ciudades_list):
    total = 0
    longitud = len(ciudades_list)
    print(ciudades_list['ciudad 1'])

    for i in range(len(ciudades_list)):
        while(longitud>=(i+1)):
            print('Distancia entre ciudad ',i+1,ciudades_list['ciudad '+str(i+1)],' y ciudad ',longitud,ciudades_list['ciudad '+str(longitud)])
            total += distance_points(ciudades_list['ciudad '+str(i+1)],ciudades_list['ciudad '+str(longitud)])
            longitud -= 1

        longitud = len(ciudades_list)

    return total