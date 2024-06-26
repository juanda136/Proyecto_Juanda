# Definimos el valor del día laboral
valor_dia = 136000

# Solicitamos al usuario la cantidad de días laborados en el mes
dias_laborados = int(input("Ingrese la cantidad de días laborados en el mes: "))

# Calculamos el salario base sin bonificaciones
salario_base = valor_dia * dias_laborados

# Inicializamos los bonos
bono = 0
bono_15_dias = 0
bono_30_dias = 0

# Verificamos si se debe aplicar el bono de $60.000
if salario_base >= 1088000:
    bono = 60000

# Verificamos si se debe aplicar el bono del 10% por más de 15 días laborados
if dias_laborados > 15 and dias_laborados < 30:
    bono_15_dias = salario_base * 0.10

# Verificamos si se debe aplicar el bono del 20% por trabajar todo el mes (30 días)
# Nota: Esto sobrescribe el bono de 10% si se cumplen ambas condiciones
if dias_laborados == 30:
    bono_15_dias = 0  # Si se trabaja todo el mes, no se aplica el bono de 15 días
    bono_30_dias = salario_base * 0.20

# Calculamos el salario total
salario_total = salario_base + bono + bono_15_dias + bono_30_dias

# Mostramos el resultado
print(f"Salario base: ${salario_base:.2f}")
print(f"Bono: ${bono:.2f}")
print(f"Bono por más de 15 días laborados: ${bono_15_dias:.2f}")
print(f"Bono por mes completo laborado: ${bono_30_dias:.2f}")
print(f"Salario total: ${salario_total:.2f}")