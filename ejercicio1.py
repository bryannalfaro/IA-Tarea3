import numpy as np

# Ingreso de los parametros por parte del usuario

def DerrivRosenbrock0 ( point ):
    dx = 2*point[0] - 400*point[0]*(point[1] - (point[0]**2))
    dy = 200*(point[1] - (point[0]**2))
    return dx, dy

def DerrivRosenbrock1 ( point ):
    dx = (-2*(1 - point[0]) - 400*(point[1] - (point[0]**2)**2))
    dy = 200*(point[1] - (point[0]**2))
    return dx, dy


funcion_objetivo = int(input('Ingrese la funcion Objetivo: '))
# gradiente = int(input('Ingrese el gradiente de la funcion: '))
punto_inicial_x = float(input('Ingrese el punto inicial en X: '))
punto_inicial_y = float(input('Ingrese el punto inicial en Y: '))
learning_rate = float(input('Ingrese el tamaño de paso: '))
numero_iteraciones = int(input('Ingrese el numero maximo de iteraciones: '))
# tolerancia = int(input('Ingrese la tolerancia: '))
# criterio = int(input('Ingrese el criterio de paro: '))

if (funcion_objetivo == 3):
    a = np.array([punto_inicial_x, punto_inicial_y])
    ai = []

    for i in range(numero_iteraciones):
        f = ((1 - a[0])**2) + (100*((a[1] - a[0]**2)**2))
        ai.append([a,f])
        fi = np.array(DerrivRosenbrock1(a))
        a = a - np.dot(learning_rate,fi)

    ai = np.array(ai)
    print(ai[-10:-1])
    print(f'the minimum is: {ai[-1, 1]} at point: {ai[-1,0]}')

