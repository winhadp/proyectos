class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f'{self.nombre} (id: {self.id} | precio: ${self.precio} | cantidad: {self.cantidad})'


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("\nya existe el id. actualizando cantidad...")
            self.productos[producto.id].cantidad += producto.cantidad
        else:
            self.productos[producto.id] = producto
            print("\nproducto agregado al inventario")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print(f"\nproucto con id {id} eliminado del inventario")
        else:
            print("\nproducto no encontrado")

    def listar_productos(self):
        if len(self.productos) == 0:
            print("\nel inventario esta vacio")
        else:
            print("\n--- tus productos ---")
            for producto in self.productos.values():
                print(producto)
            print("---------------------")


mi_inventario = Inventario()

while True:
    print("\n inventario")
    print("1. agregar producto")
    print("2. elminar producto")
    print("3. ver inventario")
    print("4. salir")
    
    opcion = input("\nelige una opion: ")

    if opcion == "1":
        mi_inventario.listar_productos()
        
        print("\n--- nevo producto ---")
        id = int(input("id del producto: "))
        nombre = input("nombre del producto: ")
        precio = float(input("precio: "))
        cantidad = int(input("cantidad: "))
        
        nuevo_p = Producto(id, nombre, precio, cantidad)
        mi_inventario.agregar_producto(nuevo_p)

    elif opcion == "2":
        mi_inventario.listar_productos()
        
        if len(mi_inventario.productos) > 0:
            id = int(input("\nid del producto a eliminar: "))
            mi_inventario.eliminar_producto(id)

    elif opcion == "3":
        mi_inventario.listar_productos()

    elif opcion == "4":
        print("\nsaliendo, chao")
        break
    else:
        print("\nopcion no valida, elige un numero del 1 al 4")