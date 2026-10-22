#este sirve para seleccionar varias opciones a la misma vex
 

import tkinter as tk

ventana = tk.Tk()
ventana.title("check button")

variable1 = tk.BooleanVar()

def cambio():
    if variable1.get():
        botton.config(state="normal")
    else:
        botton.config(state="disabled")

check1 = tk.Checkbutton(ventana, text="Opción 1", variable=variable1, command=cambio )

botton = tk.Button(ventana, text="mostrar selección", state="disabled")
botton.pack()


check1.pack()




ventana.mainloop()