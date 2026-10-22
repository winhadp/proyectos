cadena = input("por favor, introduce una cadena: ")

cadena = cadena.lower()
print(cadena)

l_cadena = list(cadena)

l_cadena_alReves = list(cadena)
l_cadena_alReves.reverse()

while " " in l_cadena:
    l_cadena.remove(" ")

while " " in l_cadena_alReves:
    l_cadena_alReves.remove(" ")


if l_cadena == l_cadena_alReves:
    print("La cadena introducida es un palindromo ")

else:
    print("La cadena introducida no es un palindromo ")
    