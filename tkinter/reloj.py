import time
import tkinter as tk

ventana = tk.Tk()
ventana.title("ej de label")

etiqueta = tk.Label(ventana, text=" primer reloj ")
etiqueta.config(bg="black", fg="white", font=("Arial", 20), width=20, height=2)
etiqueta.pack()

def actualizar_hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000, actualizar_hora)


actualizar_hora()

ventana.mainloop()