
def calculadoraa():
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Ingrese el número de la operación que desea realizar (1/2/3/4): ")

    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            resultado = num1 + num2
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == '2':
            resultado = num1 - num2
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == '3':
            resultado = num1 * num2
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"El resultado de la división es: {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")