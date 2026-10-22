import tkinter as tk


def boton_pulsado(nombre):
  print(f"{nombre}")



ventana = tk.Tk()
ventana.title("prueba de marcos y botones")
ventana.geometry("350x450")

#1
marco1 = tk.Frame(
    ventana, bg="#ffcccb", bd=2, relief="solid"
)  
marco1.pack(pady=10, padx=20, fill="x")
btn1 = tk.Button(
    marco1, text="Botón 1", command=lambda: boton_pulsado("Botón 1")
)
btn1.pack(pady=15)

#2
marco2 = tk.Frame(ventana, bg="#d0f0c0", bd=2, relief="solid")
marco2.pack(pady=10, padx=20, fill="x")
btn2 = tk.Button(
    marco2, text="Botón 2", command=lambda: boton_pulsado("Botón 2")
)
btn2.pack(pady=15)

#3
marco3 = tk.Frame(
    ventana, bg="#add8e6", bd=2, relief="solid"
)  
marco3.pack(pady=10, padx=20, fill="x")
btn3 = tk.Button(
    marco3, text="Botón 3", command=lambda: boton_pulsado("Botón 3")
)
btn3.pack(pady=15)

#4
marco4 = tk.Frame(
    ventana, bg="#ffffe0", bd=2, relief="solid"
)  
marco4.pack(pady=10, padx=20, fill="x")
btn4 = tk.Button(
    marco4, text="Botón 4", command=lambda: boton_pulsado("Botón 4")
)
btn4.pack(pady=15)


ventana.mainloop()