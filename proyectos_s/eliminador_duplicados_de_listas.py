
lista = [3, 3, 3, 6, 5, 4, 4, 3, 2, 2, 1, 3, 9 , 11]
lista_aux = []

for elemento in lista:
    if elemento not in lista_aux:
        lista_aux.append( elemento )

print( "Lista original: ", lista)
print("Lista sin duplicados: ", lista_aux)