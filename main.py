import time
import os
import random

# Posición inicial del pez
posicion = 0

# Altura inicial del pez
altura = 10

# Dirección inicial del pez
direccion = 1

# Bucle infinito para la animación
while True:
    # Limpia la terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Imprime las líneas vacías por encima del pez
    for i in range(altura):
        print()

    # Imprime el pez en la posición actual
    if direccion == 1:
        print(' ' * posicion + '><(((°>')  # Pez mirando a la derecha
    else:
        print(' ' * posicion + '<°)))><')  # Pez mirando a la izquierda

    # Imprime las líneas vacías por debajo del pez
    for i in range(20 - altura):
        print()

    # Cambia la posición y la dirección del pez
    posicion += direccion
    if posicion == 0 or posicion == 100:
        direccion = -direccion
        altura = random.randint(0, 20)  # Cambia la altura del pez al azar

    # Espera un poco antes del siguiente cuadro
    time.sleep(0.05)
