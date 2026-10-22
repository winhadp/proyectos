import tkinter as tk


def on_click(event):
    print("¡Botón presionado!")
ventana = tk.Tk()

button = tk.Button(ventana, text="presioname")
button.pack()



button.bind("<Button-1>", on_click)

def on_ki_pss(event):
    if event.char == "a":
        print("¡Has presionado la tecla 'a'!")
    

ventana.bind("<KeyPress>", on_ki_pss)


ventana.mainloop()