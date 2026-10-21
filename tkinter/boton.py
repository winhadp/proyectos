
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Ventana")

boton = tk.Button(ventana, text="Presioname")

boton.config(bg="blue", fg="white", font=("Arial", 16))

boton.pack()

etiqueta = tk.Label(ventana, text="Hola")
etiqueta.pack()

def cambiar_texto():
    etiqueta.config(text="Has presionado el botón.")

boton.config(command=cambiar_texto)

ventana.mainloop()