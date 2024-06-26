# Función para calcular la nota final basada en los valores de los tres parciales
def calcular_notaf(primer_parcial, segundo_parcial, tercer_parcial):
    return (primer_parcial * 0.25) + (segundo_parcial * 0.20) + (tercer_parcial * 0.55)

# Función para solicitar una nota válida entre 0 y 5.0
def solicitar_nota(parcial_numero):
    while True:
        try:
            nota = float(input(f"Ingresa la nota del {parcial_numero} parcial (de 0 a 5.0): "))
            if 0 <= nota <= 5:
                return nota
            else:
                print("Error: El valor no es el permitido. Por favor ingresa una nota válida entre 0 y 5.0.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

# Solicitar  cantidad de estudiantes
cantidad_estudiantes = int(input("Ingresa la cantidad de estudiantes: "))

# Diccionario para almacenar las notfinal de los estudiantes x asignatura
notas_por_asignatura = {}

# buqle q ingresar datos de cada estudiante
for i in range(cantidad_estudiantes):
    print(f"\nEstudiante {i + 1}:")
    nombre = input("Ingresa tu nombre: ")
    asignatura = input("Ingresa la asignatura: ")

    # Solicitar notas validadas
    primer_parcial = solicitar_nota("primer")
    segundo_parcial = solicitar_nota("segundo")
    tercer_parcial = solicitar_nota("tercer")

    # Calcular la nota final
    notaf = calcular_notaf(primer_parcial, segundo_parcial, tercer_parcial)

    # Mostrar la nota final junto con el nombre y la asignatura del usuario
    print(f"La nota final de {nombre} en la asignatura {asignatura} es {notaf:.2f}")

    # Almacenar la notaf en el diccionario x asignatura
    if asignatura not in notas_por_asignatura:
        notas_por_asignatura[asignatura] = []
    notas_por_asignatura[asignatura].append(notaf)

# Calcular y mostrar la nota más alta y el promedio x asignatura
for asignatura, notas in notas_por_asignatura.items():
    if notas:
        nota_mas_alta = max(notas)
        promedio_notas = sum(notas) / len(notas)
        print(f"\nAsignatura: {asignatura}")
        print(f"La nota más alta de la asignatura es {nota_mas_alta:.2f}")
        print(f"El promedio de notas de la asignatura es {promedio_notas:.2f}")






