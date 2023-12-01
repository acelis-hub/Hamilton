import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Ecuaciones diferenciales de primer orden para el sistema de coordenadas polares
def edos(theta, theta_dot, r, r_dot, t, g, k, m, a, max_length, min_length):
    dtheta_dt = theta_dot
    dr_dt = r_dot
    dtheta_dot_dt = (g * np.sin(theta) - 2 * theta_dot) / r
    force_spring = (k / m) * (r - a)
    
    # Restringe la longitud del resorte en ambas direcciones
    if r > max_length:
        force_spring = 0
        r_dot = -abs(r_dot)  # Invierte la velocidad para evitar un cambio brusco
    elif r < min_length:
        force_spring = 0
        r_dot = abs(r_dot)  # Invierte la velocidad para evitar un cambio brusco
        r = min_length  # Ajuste para evitar que la longitud del resorte sea menor que el mínimo

    # Restringe el movimiento hacia el eje positivo
    if r_dot > 0:
        force_spring = 0
        r_dot = 0

    dr_dot_dt = -(force_spring + g * np.cos(theta)) / r
    return dtheta_dt, dtheta_dot_dt, dr_dt, dr_dot_dt

# Aplicación del método de Euler
def metodo_euler(theta0, theta_dot0, r0, r_dot0, t, g, k, m, a):
    num_pasos = len(t)
    resultados_theta = np.zeros(num_pasos)
    resultados_theta_dot = np.zeros(num_pasos)
    resultados_r = np.zeros(num_pasos)
    resultados_r_dot = np.zeros(num_pasos)

    resultados_theta[0] = theta0
    resultados_theta_dot[0] = theta_dot0
    resultados_r[0] = r0
    resultados_r_dot[0] = r_dot0

    for i in range(1, num_pasos):
        dt = t[i] - t[i-1]
        dtheta_dt, dtheta_dot_dt, dr_dt, dr_dot_dt = edos(resultados_theta[i-1],
                                                   resultados_theta_dot[i-1],
                                                   resultados_r[i-1],
                                                   resultados_r_dot[i-1],
                                                   t[i-1], g, k, m, a, max_length, min_length)

        theta0 = theta0 + dt * dtheta_dt
        theta_dot0 = theta_dot0 + dt * dtheta_dot_dt
        r0 = r0 + dt * dr_dt
        r_dot0 = r_dot0 + dt * dr_dot_dt

        resultados_theta[i] = theta0
        resultados_theta_dot[i] = theta_dot0
        resultados_r[i] = r0
        resultados_r_dot[i] = r_dot0

    return resultados_theta, resultados_theta_dot, resultados_r, resultados_r_dot

# Definición de la secuencia de tiempo explícito
tiempo_explicito = np.linspace(0, 20, 2000)

# Parámetros
min_length = 5
max_length = 10
theta0 = np.pi / 80  # Condición inicial para el ángulo theta
theta_dot0 = 0  # Condición inicial para la velocidad angular
r0 = 8.1  # Condición inicial para la distancia radial
r_dot0 = 0  # Condición inicial para la velocidad radial
g = 9.8  # Aceleración debido a la gravedad
k = 0.1  # Constante del resorte
m = 1  # Masa
a = 8  # Longitud de equilibrio del resorte

# Aplicación del método de Euler
resultados_theta, resultados_theta_dot, resultados_r, resultados_r_dot = \
    metodo_euler(theta0, theta_dot0, r0, r_dot0, tiempo_explicito, g, k, m, a)

# Crear una animación
fig, ax = plt.subplots()
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
line1, = ax.plot([], [], 'b', lw=2)  # Crea el resorte
techo, = ax.plot([], [], 'k:', lw=1)  # Crea el techo
point, = ax.plot([], [], 'ro')  # Crea la bola

def init():
    line1.set_data([], [])
    techo.set_data([], [])
    point.set_data([], [])
    return line1, point, techo


def update(frame):
    x1 = resultados_r[frame] * np.sin(resultados_theta[frame])
    y1 = -resultados_r[frame] * np.cos(resultados_theta[frame])
    
    # Actualiza la posición del resorte y la cuerda
    line1.set_data([0, x1], [0, y1])
    
    # Restringe la longitud mínima del resorte visualmente
    if resultados_r[frame] < min_length:
        resultados_r[frame] = min_length

    # Actualiza la posición de la bola
    point.set_data(x1, y1)

    # Actualiza el techo
    techo.set_data([-5, 5], [0, 0])

    return line1, point, techo

ani = FuncAnimation(fig, update, frames=len(tiempo_explicito), init_func=init, blit=True, interval=16)
ani.save('Segundo_Problema.mp4', writer='ffmpeg', fps=30)
plt.show()
