def calcular_imc(altura, peso):

    return peso / (altura**2)



altura = float(input("porfavor introduce tu altura en metros: "))
peso = float(input("porfavor introduce tu peso en kg: "))

imc = calcular_imc(altura, peso)

if imc < 18.5:
    print("peso insuficiente")
elif imc >= 18.5 and imc < 24.9:
    print("peso suficiente")
elif imc >= 24.9 and imc < 29.9:
    print("sobrepeso")
elif imc >= 29.9 and imc < 34.9:
    print("obesidad")
else:
    print("obesidad morbida")


print(f"{imc:.2f}")




