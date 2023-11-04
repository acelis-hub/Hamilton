import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

# ecuaciones diferenciales de primer orden
def edos(th, w, t, l, u, g):
	dth_dt = w
	dw_dt = (1/(l-u*t))*(2*u*w-g*np.sin(th))
	return dth_dt, dw_dt

# aplicación del metodo de euler
def metodo_euler(th0, w0, l, u, g, tiempo):
	num_pasos = len(tiempo)
	resultados_th = np.zeros(num_pasos) # inicializa lista
	resultados_w = np.zeros(num_pasos) # inicializa lista

	resultados_th[0] = th0 # condición inicial
	resultados_w[0] = w0 # condición inicial

	for i in range(1, num_pasos):
		dt = tiempo[i] - tiempo[i-1] # tamaño paso de tiempo
		dth_dt, dw_dt = edos(resultados_th[i-1], # calcula los diferenciales de movimiento
							 resultados_w[i-1],
							 tiempo[1-i],
							 l, u, g)
		th0 = th0 + dt*dth_dt # actualiza la posición
		w0 = w0 + dt*dw_dt # actualiza la velocidad
		resultados_th[i] = th0
		resultados_w[i] = w0

	return resultados_th, resultados_w

# Definición secuencia de tiempo explicito

tiempo_explicito = np.linspace(0,50,1000000) # duración de 50 seg, un millon de datos

## Parametros
th0 = np.pi / 8 # Condición inicial para el angulo theta
w0 = 0 # Condición inicial para la velocidad angular
l = 10 # longitud de la cuerda
u = 0.15 # velocidad de la cuerda
g = 9.8 # gravedad

# Aplicación metodo de Euler
resultados_th, resultados_w = metodo_euler(th0,w0, l, u, g, tiempo_explicito)

# Grafica de resultados
plt.plot(tiempo_explicito, (180/np.pi)*resultados_th, label='theta(t)')
plt.plot(tiempo_explicito, (180/np.pi)*resultados_w, label='w(t)')
plt.xlabel('tiempo')
plt.legend()
plt.show()
