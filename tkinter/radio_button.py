#solo usamos cuando queremos una sola opcion 
import tkinter as tk

ventana = tk.Tk()
ventana.title("boton de opcion")

variable_control = tk.IntVar()

def color():
    color_seleccionado = variable_control.get()
    if color_seleccionado == 1:
        ventana.config(bg="yellow")
    elif color_seleccionado == 2:
        ventana.config(bg="pink")

opcion1 = tk.Radiobutton(ventana, text="Opción 1 yellow", variable=variable_control, value=1, command=color)
opcion1.pack()
opcion2 = tk.Radiobutton(ventana, text="Opción 2 pink ", variable=variable_control, value=2, command=color)
opcion2.pack()

def selecion ():
    print("Opción seleccionada:", variable_control.get())

boton = tk.Button(ventana, text="mostrar selección", command=selecion)
boton.pack()

ventana.mainloop()