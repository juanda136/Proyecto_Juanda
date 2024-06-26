# Definir la estructura para almacenar los datos de los estudiantes
class Estudiante:
    def __init__(self, cedula, nombre, salario, edad, sexo, carrera):
        self.cedula = cedula
        self.nombre = nombre
        self.salario = salario
        self.edad = edad
        self.sexo = sexo
        self.carrera = carrera

# Lista para almacenar los estudiantes
estudiantes = []

# Cantidad de datos a leer (puedes cambiar esto por la cantidad deseada)
#constructor
cantidad_de_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

# Lectura de datos
for _ in range(cantidad_de_estudiantes):
    cedula = input("Ingrese la cédula del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    salario = float(input("Ingrese el salario del estudiante: "))
    edad = int(input("Ingrese la edad del estudiante: "))
    sexo = int(input("Ingrese el sexo del estudiante (1:Femenino, 2:masculino)"))
    estado_civil =int(input( "ingrese su estado civil (1:Soltero, 2:Casado, 3:Divorciado2)"))
    carrera = int(input("Ingrese la carrera del estudiante (1:Administración, 2:Derecho, 3:Medicina, 4:Sistemas): "))
    
    # Crear el objeto Estudiante y agregarlo a la lista
    estudiante = Estudiante(cedula, nombre, salario, edad, sexo, carrera)
    estudiantes.append(estudiante)

# Inicializar contadores y acumuladores
total_por_carrera = [0, 0, 0, 0]  # Contadores para cada carrera
salarios_administracion = []  # Lista de salarios para Administración
mujeres_sistemas = 0  # Contador de mujeres en Sistemas
total_sistemas = 0  # Contador total de alumnos en Sistemas
mayor_salario_medicina = 0  # Variable para el mayor salario en Medicina
edad_mayor_salario_medicina = 0  # Edad del estudiante con mayor salario en Medicina

# Procesar cada estudiante
for estudiante in estudiantes:
    # Total de alumnos por carrera
    if estudiante.carrera == 1:
        total_por_carrera[0] += 1
        salarios_administracion.append(estudiante.salario)
    elif estudiante.carrera == 2:
        total_por_carrera[1] += 1
    elif estudiante.carrera == 3:
        total_por_carrera[2] += 1
        if estudiante.salario > mayor_salario_medicina:
            mayor_salario_medicina = estudiante.salario
            edad_mayor_salario_medicina = estudiante.edad
    elif estudiante.carrera == 4:
        total_por_carrera[3] += 1
        total_sistemas += 1
        if estudiante.sexo == 1:  # Sexo Femenino
            mujeres_sistemas += 1

# Calcular la carrera con más alumnos
carreras = ["Administración", "Derecho", "Medicina", "Sistemas"]
carrera_con_mas_alumnos = carreras[total_por_carrera.index(max(total_por_carrera))]

# Calcular el promedio de salario de los alumnos de Administración
if len(salarios_administracion) > 0:
    promedio_salarios_administracion = sum(salarios_administracion) / len(salarios_administracion)
else:
    promedio_salarios_administracion = 0

# Calcular el porcentaje de mujeres en Sistemas
if total_sistemas > 0:
    porcentaje_mujeres_sistemas = (mujeres_sistemas / total_sistemas) * 100
else:
    porcentaje_mujeres_sistemas = 0

# Imprimir los resultados
print("\nResultados:")
print(f"Total de alumnos por carrera:")
for i, carrera in enumerate(carreras):
    print(f"{carrera}: {total_por_carrera[i]}")

print(f"\nCarrera con más alumnos: {carrera_con_mas_alumnos}")

print(f"\nPromedio de salario de los alumnos de Administración: ${promedio_salarios_administracion:.2f}")

print(f"\nPorcentaje de mujeres en Sistemas respecto al total de alumnos de Sistemas: {porcentaje_mujeres_sistemas:.2f}%")

if mayor_salario_medicina > 0:
    print(f"\nEdad de la persona con mayor salario en Medicina: {edad_mayor_salario_medicina}")
else:
    print(f"\nNo hay datos disponibles para Medicina.")
