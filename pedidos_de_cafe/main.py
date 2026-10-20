from historial import ver_historial
from menu import mostrar_menu
from pedidos import pedir_cafe


def main():
    while True:
        mostrar_menu()
        opcion = input("selcciona una opcion: ")

        if opcion == "1":
            pedir_cafe()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("\n muchas gracias por haber tomado nuestros cafes")
            break
        else:
            print("opcion invalida ")


if __name__ == "__main__":
    main()