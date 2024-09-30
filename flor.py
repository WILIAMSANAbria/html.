import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear una figura y ejes
fig, ax = plt.subplots()
ax.set_facecolor('skyblue')  # Color de fondo del cielo

# Limitar los ejes
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)

# Parámetros para la flor
num_petals = 8  # Número de pétalos
flower_base_size = 5  # Tamaño base de la flor
petal_color = 'yellow'
center_color = 'orange'

# Crear coordenadas para los pétalos
theta = np.linspace(0, 2 * np.pi, num_petals, endpoint=False)

# Función para actualizar cada frame
def update(frame):
    ax.clear()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_facecolor('skyblue')

    # Animar expansión y contracción de los pétalos
    radius = flower_base_size + 2 * np.sin(frame * 0.1)  # Expansión y contracción
    rotation = frame * 0.05  # Rotación constante de los pétalos
    movement_radius = 2 * np.sin(frame * 0.05)  # Movimiento oscilante de la flor

    # Coordenadas de movimiento de la flor (oscilante en círculo)
    flower_x = movement_radius * np.cos(frame * 0.05)
    flower_y = movement_radius * np.sin(frame * 0.05)

    for i in range(num_petals):
        # Coordenadas de los pétalos
        x = flower_x + radius * np.cos(theta[i] + rotation)
        y = flower_y + radius * np.sin(theta[i] + rotation)
        petal = plt.Circle((x, y), 2, color=petal_color, ec='black')
        ax.add_patch(petal)

    # Crear el centro de la flor
    center = plt.Circle((flower_x, flower_y), 1.5, color=center_color)
    ax.add_patch(center)

# Crear la animación
anim = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

# Mostrar la animación
plt.show()
