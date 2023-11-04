import numpy as np
import matplotlib.pyplot as plt
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

tiempo_explicito = np.linspace(0,50,1000) # duración de 50 seg, un millon de datos

## Parametros
th0 = np.pi / 80 # Condición inicial para el angulo theta
w0 = 0 # Condición inicial para la velocidad angular
l = 10 # longitud de la cuerda
u = 0.14 # velocidad de la cuerda
g = 9.8 # gravedad

# Aplicación metodo de Euler
resultados_th, resultados_w = metodo_euler(th0,w0, l, u, g, tiempo_explicito)

# Crear una animación
fig, ax = plt.subplots()
ax.set_xlim(-12, 12) # dimenciones de la pantalla
ax.set_ylim(-12, 12)
line1, = ax.plot([], [],'b',lw=2) # crea la cuerda
line2, = ax.plot([], [],'b',lw=2) # crea la cuerda
techo, = ax.plot([], [], 'k:', lw=1) # crea el techo
point, = ax.plot([], [], 'ro') # crea la bola

def init():
    line1.set_data([],[]) # inicializa la cuerda
    line2.set_data([],[]) # inicializa la cuerda
    techo.set_data([],[]) # inicializa el techo
    point.set_data([],[]) # inicializa el punto
    return line1, line2, point, techo

def update(frame):
    x1 = (l-(u*tiempo_explicito[frame]))*np.sin(resultados_th[frame])
    y1 = (-l+(u*tiempo_explicito[frame]))*np.cos(resultados_th[frame])
    y2 = u*tiempo_explicito[frame]
    line1.set_data([0, x1], [0, y1])  # actualiza la posición de la cuerda
    line2.set_data([0,0], [0,y2])
    techo.set_data([-5,5],[0,0]) # actualiza el techo
    point.set_data(x1, y1)  # actualiza la posición del punto
    return line1, line2, point, techo

ani = FuncAnimation(fig, update, frames=len(tiempo_explicito), init_func=init, blit=True, interval=16)
plt.show()