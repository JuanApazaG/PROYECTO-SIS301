#importamos 3 clases
from tkinter import Tk, Label, Button

#funcion mensaje con un print imprime el mensaje boton cuando le demos click al botton
def mensaje():
    print ("Mensaje del boton")

#creamos el objeto ventana a partir de una clase TK
ventana = Tk()
#damos el tamaño a la ventana
ventana.geometry ("400x280")
#titulo que tendra la ventana
ventana.title("Ventana Hola mundo")

#creamos el objeto lbl a partir de una clase Label,en el constructor primer parametro le pasamos el contenedor ventana y como titulo va tener este es un label
lbl = Label(ventana, text = "Este es un [Label] tkinter",fg="red",bg="blue")
#lo llamamos para que lbl se posisione en la ventana
lbl.pack()

#creamos el objeto btn a partir de una clase Button, en el contructor primero tendra el parametro  del contenedor de la ventana y como titulo presiona este button para mensaje, le indicamos que cuando se de click al botton se ejecuta la funcion mensaje
btn = Button(ventana, text="Presiona este [button] para mensaje", command = mensaje)
#btn.config(fg="red",bg="orange")
btn["bg"]="orange"
btn['fg'] = "white"
btn.pack()

#se corre el ciclo de la ventana
ventana.mainloop()