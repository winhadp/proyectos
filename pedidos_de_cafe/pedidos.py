ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\n Elige el cafe que quieras")
    print("1. expreso")
    print("2. capuchino")
    print("3. negro")
    print("4. mocha")
    
    opion = input("Opcion: ")
    
    cafes = {
        "1" : "expreso",
        "2" : "capuchino",
        "3" : "negro",
        "4" : "mocha",

    }
    if opion in cafes:
        cafe_elegido = cafes[opion]
        print("Has pedidio un " + cafe_elegido  + ". ¡Preparando tu cafe!")

        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("la opcion no es valida")