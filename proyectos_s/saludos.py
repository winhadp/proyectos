def saludar(nombre):
    print(f"Hola, {nombre}!")
saludar("Andrés")
saludar("Camilo")
saludar("carlos")

def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num 
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    print(contraseña)
   
crear_contraseña_random(94)



    
