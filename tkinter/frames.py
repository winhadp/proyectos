import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi Ventana")
ventana.geometry("400x300")
ventana.config(bg="lightblue")

frame1 = tk.Frame(ventana)
frame1.config(bg="red", width=200, height=150, bd=5)
frame1.pack()

frame2 = tk.Frame(frame1)
frame2.config(bg="blue", width=200, height=150, bd=2)
frame2.pack()

boton = tk.Button(frame1, text="Haz clic aquí")
boton.pack()


 

ventana.mainloop()