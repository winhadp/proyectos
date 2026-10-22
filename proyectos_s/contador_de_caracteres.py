cadena = input("por favor introduce una cadena de caracteres: ")
cadena = cadena.lower()

caracteres = {}

for caracter in cadena:

    if caracter in caracteres:
        caracteres[caracter] += 1
    else:
        caracteres[caracter] = 1

print(caracteres)