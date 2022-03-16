import numpy as np
from matplotlib import pyplot as plt

def funcion_a(param):
  return (param[0]**4) + (param[1]**4) - (4*param[0]*param[1]) + (0.5*param[1]) + 1

def derivada_a(param):
  return (4*(param[0]**3) - 4*param[1])*np.array([1., 0.]) + (4*(param[1]**3) - 4*param[0] + 0.5)*np.array([0., 1.])

def funcion_b(param):
  return 100*(param[1] - param[0]**2)**2 + (1 - param[0])**2

def derivada_b(param):
  return (400*param[0]**3 - 400*param[0]*param[1] + 2*param[0] - 2)*np.array([1., 0.]) + (200*(param[1] - param[0]**2))*np.array([0., 1.])

def funcion_c(param):
  count = 0
  suma = 0
  while count != 9:
    suma += funcion_b([param[count], param[count+1]])
    count = count + 1
  return suma

def derivada_c(param):
  lista = []
  lista.append(derivada_b([param[0], param[1]])[0])

  for i in range(1, 9):
    x, y, z = param[i-1], param[i], param[i+1]
    di = 200*(z - y**2)*(-2*y) - 2*(1 - y) + 200*(y - x**2)
    lista.append(di)
  lista.append(200*(param[9] - param[8]**2))

  return np.array(lista)

def graficar(data):
  plt.figure()
  plt.title('Grafica')
  plt.plot(data[1:len(data)])
  plt.xlabel('x')
  plt.ylabel('Error')
  plt.show()