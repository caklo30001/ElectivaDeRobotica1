
#1. Realice un programa que calcule la potencia que consume un circuito ingresando por teclado el
#valor de corriente y voltaje.

print("=== CÁLCULO DE POTENCIA ELÉCTRICA ===")

try:
    voltaje = float(input("Ingrese el voltaje (V): "))
    corriente = float(input("Ingrese la corriente (A): "))

    potencia = voltaje * corriente

    print(f"\nLa potencia consumida es: {potencia} Watts")

except ValueError:
    print("Error: Debe ingresar valores numéricos.")
#2. Realice un programa que calcule X números aleatorios en un rango determinado por el usuario. 

import math

print("=== CÁLCULO DE VOLÚMENES ===")
print("1. Prisma")
print("2. Pirámide")
print("3. Cilindro")
print("4. Cono truncado")

opcion = int(input("Seleccione la figura (1-4): "))

match opcion:

    case 1:  # Prisma
        area_base = float(input("Ingrese el área de la base: "))
        altura = float(input("Ingrese la altura: "))
        volumen = area_base * altura
        print(f"El volumen del prisma es: {volumen}")

    case 2:  # Pirámide
        area_base = float(input("Ingrese el área de la base: "))
        altura = float(input("Ingrese la altura: "))
        volumen = (area_base * altura) / 3
        print(f"El volumen de la pirámide es: {volumen}")

    case 3:  # Cilindro
        radio = float(input("Ingrese el radio: "))
        altura = float(input("Ingrese la altura: "))
        volumen = math.pi * radio**2 * altura
        print(f"El volumen del cilindro es: {volumen}")

    case 4:  # Cono truncado
        R = float(input("Ingrese el radio mayor (R): "))
        r = float(input("Ingrese el radio menor (r): "))
        altura = float(input("Ingrese la altura: "))
        volumen = (1/3) * math.pi * altura * (R**2 + r**2 + R*r)
        print(f"El volumen del cono truncado es: {volumen}")

    case _:
        print("Opción no válida.")

#3. Realice un programa para el cálculo de volúmenes (Prisma, Pirámide, Cono truncado, Cilindro)
#donde el usuario pueda seleccionar el sólido y los parámetros de cada volumen. 

print("=== TIPOS DE ROBOTS INDUSTRIALES ===")
print("1. Robot Cartesiano")
print("2. Robot Cilíndrico")
print("3. Robot Esférico")

opcion = int(input("Seleccione el tipo de robot (1-3): "))

match opcion:

    case 1:
        print("\nRobot Cartesiano")
        print("Tipo de articulaciones: 3 prismáticas (PPP)")
        print("Número de articulaciones: 3")

    case 2:
        print("\nRobot Cilíndrico")
        print("Tipo de articulaciones: 1 rotacional + 2 prismáticas (RPP)")
        print("Número de articulaciones: 3")

    case 3:
        print("\nRobot Esférico")
        print("Tipo de articulaciones: 2 rotacionales + 1 prismática (RRP)")
        print("Número de articulaciones: 3")

    case _:
        print("Opción no válida.")

#4. Realice un programa que le permita al usuario escoger entre robot Cilíndrico, Cartesiano y esférico,
#donde como respuesta a la selección conteste con el tipo y número de articulaciones que posee.


while True:
    resp = input("¿Desea continuar? (Si/No): ").strip().lower()

    if resp in ("no", "n"):
        print("Programa finalizado.")
        break
    elif resp in ("si", "sí", "s"):
        print("Continuando...\n")
    else:
        print("Entrada no válida. Escriba Si o No.\n")


#5. Escribir un programa que realice la pregunta ¿Desea continuar Si/No? y que no deje de hacerla
#hasta que el usuario teclee No.


import random

try:
    cantidad = int(input("¿Cuántos números aleatorios quieres generar?: "))
    minimo = int(input("Ingrese el límite mínimo: "))
    maximo = int(input("Ingrese el límite máximo: "))

    if minimo > maximo:
        print("Error: El límite mínimo no puede ser mayor que el máximo.")
    else:
        print("\nNúmeros generados:\n")
        for i in range(cantidad):
            numero = random.randint(minimo, maximo)
            print(f"Número {i+1}: {numero}")

except ValueError:
    print("Error: Debes ingresar valores numéricos enteros.")
