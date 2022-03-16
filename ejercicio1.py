import numpy as np
import funciones as f

# PARTES DEL CODIGO SE OBTUVIERON DE https://realpython.com/gradient-descent-algorithm-python/

def descenso_maximo(funcion, derivada, punto, alfa, iteraciones, tolerancia=1e-4):
#   Inicializacion de variables
  n_count = 0
  convergencia = 0
  bandera = 0
# Se inicializan las listar a utilizar
  valores = [punto]
  res = [funcion(punto)]
  norm = [np.linalg.norm(punto, 1)]
#   Copia del punto
  copia = punto.copy()
# Ciclo que revisa las iteraciones
  while (bandera == 0 and n_count < iteraciones):
    anterior = copia
    copia = anterior - alfa*derivada(anterior)
    error = np.linalg.norm(anterior - copia, 2)

    if (error < tolerancia):
      convergencia = 1
      bandera = 1

    # Se agregan los valores a las listas
    valores.append(copia)
    res.append(funcion(copia))
    norm.append(error)

    n_count += 1
  
  return [res[-1], norm, valores, res, n_count, convergencia]

# IMPRESION DEL MENU PARA EL USUARIO
funcion_objetivo = int(input('Ingrese la funcion Objetivo: '))
numero_iteraciones = int(input('Ingrese el numero maximo de iteraciones: '))
alfa = float(input('Ingrese alfa: '))
punto_inicial_x = float(input('Ingrese el punto inicial en X: '))
punto_inicial_y = float(input('Ingrese el punto inicial en Y: '))

# Validacion de el input del usuario
if funcion_objetivo == 1:
  minimo, errores, valores, res, n_count, convergencia = descenso_maximo(f.funcion_a, f.derivada_a, np.array([punto_inicial_x, punto_inicial_y]), alfa, numero_iteraciones)
  f.graficar(errores)
elif funcion_objetivo == 2:
  minimo, errores, valores, res, n_count, convergencia = descenso_maximo(f.funcion_b, f.derivada_b, np.array([punto_inicial_x, punto_inicial_y]), alfa, numero_iteraciones)
  f.graficar(errores)
elif funcion_objetivo == 3:
  p3 = float(input('Ingrese el punto 3: '))
  p4 = float(input('Ingrese el punto 4: '))
  p5 = float(input('Ingrese el punto 5: '))
  p6 = float(input('Ingrese el punto 6: '))
  p7 = float(input('Ingrese el punto 7: '))
  p8 = float(input('Ingrese el punto 8: '))
  p9 = float(input('Ingrese el punto 9: '))
  p10 = float(input('Ingrese el punto 0: '))
  minimo, errores, valores, res, n_count, convergencia = descenso_maximo(f.funcion_c, f.derivada_c, np.array([punto_inicial_x, punto_inicial_y, p3, p4, p5, p6, p7, p8, p9, p10]), alfa, numero_iteraciones)
  f.graficar(errores)
print('Mejor solucion encontrada: ', minimo)
print('Secuencia de valores: ', valores)
print('Secuencia de Iteraciones: ', res)
print('Numero de iteraciones: ', n_count)
print('Convergencia: ', convergencia)
print('Primeras 4 X_k', valores[0], valores[1], valores[2], valores[3])
print('Ultimas 4 X_k', valores[len(valores)-1], valores[len(valores)-2], valores[len(valores)-3], valores[len(valores)-4])