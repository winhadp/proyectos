animales = ["vaca", "gato", "perro", "elefante", "jirafa"]

for animal in animales:
    print(f'ahora la variable aniaml es igual : {animal}')

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    resultado = numero * 2
    print(resultado)

for numero, animal in zip(numeros, animales):
    print(f'El numero es {numero} ')
    print(f'El animal es {animal} ')

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es {indice} ')
    print(f'El valor es {valor} ')

for numero in numeros:
    print(f'Ultimo bucle: {numero} ')
print('El bucle ha finalizado')


    #bucle while
contador = 0
while contador < 10:
    print(contador)
    contador += 1

    print('El bucle while ha finalizado')

    