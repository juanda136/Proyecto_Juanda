# # Inicialización del tablero
# tablero = [" " for i in range(9)]
# # Función para imprimir el tablero
# def print_triki():
#     for fila in range(3):
#         linea = f"|{tablero[fila*3]}|{tablero[fila*3+1]}|{tablero[fila*3+2]}|"
#         print(linea)

# # Función para manejar el turno de un jugador
# def jugador(turno):
#     if turno == 'X':
#         num = 1
#     else:
#         num = 2
#     print(f"\nTu turno jugador #{num} ({turno})")
    
#     while True:
#         try:
#             eleccion = int(input('Ingresa tu movimiento (1-9): ').strip())
#             if 1 <= eleccion <= 9:
#                 if tablero[eleccion - 1] == " ":
#                     tablero[eleccion - 1] = turno
#                     break
#                 else:
#                     print("El espacio está ocupado, intenta de nuevo.\n")
#             else:
#                 print("Movimiento inválido, ingresa un número entre 1 y 9.\n")
#         except ValueError:
#             print("Movimiento inválido, ingresa un número válido.\n")

# # Función para verificar si un jugador ha ganado
# def ganador(icono):
#     combinaciones_ganadoras = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
#         [0, 4, 8], [2, 4, 6]              # Diagonales
#     ]
#     for combinacion in combinaciones_ganadoras:
#         if all(tablero[pos] == icono for pos in combinacion):
#             return True
#     return False

# # Función para verificar si hay un empate
# def empate():
#     return " " not in tablero

# # Lógica principal del juego
# while True:
#     print_triki()
#     jugador("X")
#     if ganador('X'):
#         print_triki()
#         print("¡FELICITACIONES jugador 1, has ganado!")
#         break
#     elif empate():
#         print_triki()
#         print("¡Es un empate!")
#         break
    
#     print_triki()
#     jugador("O")
#     if ganador('O'):
#         print_triki()
#         print("¡FELICITACIONES jugador 2, has ganado!")
#         break
#     elif empate():
#         print
#EJERCICIO CAMBIANDO JUAGADOR POR NOMBRE.
              # Inicialización del tablero
tablero = [" " for _ in range(9)]

# Solicitar los nombres de los jugadores
nombre_jugador1 = input("Ingrese el nombre del jugador 1 (X): ").strip()
nombre_jugador2 = input("Ingrese el nombre del jugador 2 (O): ").strip()

# Función para imprimir el tablero
def print_triki():
    for fila in range(3):
        linea = f"|{tablero[fila*3]}|{tablero[fila*3+1]}|{tablero[fila*3+2]}|"
        print(linea)
    print("-" * 13)

# Función para manejar el turno y nombre del un jugador
def jugador(turno, nombre):
    print(f"\n{nombre}, es tu turno ({turno})")
    
    while True:
        try:
            eleccion = int(input('Ingresa tu movimiento (1-9): ').strip())
            if 1 <= eleccion <= 9:
                if tablero[eleccion - 1] == " ":
                    tablero[eleccion - 1] = turno
                    break
                else:
                    print("El espacio está ocupado, intenta de nuevo.\n")
            else:
                print("Movimiento inválido, ingresa un número entre 1 y 9.\n")
        except ValueError:
            print("Movimiento inválido, ingresa un número válido.\n")

# Función para verificar si un jugador ha ganado
def ganador(icono):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combinacion in combinaciones_ganadoras:
        if all(tablero[pos] == icono for pos in combinacion):
            return True
    return False

# Función para verificar si hay un empate
def empate():
    return " " not in tablero

# Lógica principal del juego
while True:
    print_triki()
    jugador("X", nombre_jugador1)
    if ganador('X'):
        print_triki()
        print(f"¡FELICITACIONES {nombre_jugador1}, has ganado!")
        break
    elif empate():
        print_triki()
        print("¡Es un empate!")
        break
    
    print_triki()
    jugador("O", nombre_jugador2)
    if ganador('O'):
        print_triki()
        print(f"¡FELICITACIONES {nombre_jugador2}, has ganado!")
        break
    elif empate():
        print_triki()
        print("¡Es un empate!")
        break
