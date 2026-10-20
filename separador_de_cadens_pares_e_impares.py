
cadena = input("Introduce una cadena de caracteres: ")

pares = ""
impares = ""

contador = 0
while contador < len(cadena):

    if contador % 2 == 0:
        impares = impares + cadena[contador]
    else:
        pares = pares + cadena[contador]

    contador += 1
        
print("Cadena original: ", cadena)
print("Caracteres en posiciones pares: ", pares)
print("Caracteres en posiciones impares: ", impares)