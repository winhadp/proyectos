
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Ventana")

etiqueta = tk.Label(ventana, text="Hola soy un label ")
etiqueta.pack()


entrada = tk.Entry(ventana)
entrada.pack()
entrada.insert(0, "Escribe algo aquí")
texto = entrada.get()
print(texto)

def aplicar_texto():
    texto = entrada.get()
    etiqueta.config(text=texto)

boton_aplicar = tk.Button(ventana, text="Aplicar", command=aplicar_texto)
boton_aplicar.pack()


ventana.mainloop()