
def separar_pares_impares(numeros):

    lista_pares, lista_impares = [], []
    for numero in numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)

    return lista_pares, lista_impares

mi_lista = [89, 70, 55, 67, 98, 47, 72, 80, 19, 10]

print("Lista original es :", mi_lista)

lista_pares, lista_impares = separar_pares_impares(mi_lista)
print("Lista de números pares:", lista_pares)
print("Lista de números impares:", lista_impares)