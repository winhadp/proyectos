def mcm(numero1, numero2):
    if numero1 > numero2:
        num_mayor = numero1
    else:
        num_mayor = numero2

    while (num_mayor % numero1) != 0 or (num_mayor % numero2) != 0:
        num_mayor += 1

    return num_mayor


# Bloque para pedir los números por la terminal
try:
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

    resultado = mcm(num1, num2)
    print(f"El Mínimo Común Múltiplo (MCM) es: {resultado}")
except ValueError:
    print("Por favor, ingresa solo números enteros válidos.")