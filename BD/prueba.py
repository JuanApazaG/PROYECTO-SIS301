#pylint: disable=unused-import
#import mysql.connector


# Importamos el módulo ttk de tkinter, que nos permitirá usar widgets avanzados como botones y campos de entrada
from tkinter import ttk
# Importamos el módulo tkinter para construir la interfaz gráfica de usuario
from tkinter import *
# Importamos la biblioteca sqlite3, que nos permitirá interactuar con una base de datos SQLite
import sqlite3

class Productos:
    
    #Variable para la BD
    base = 'Productos.db'

    # Definimos un método "__init__" que se ejecutará automáticamente al crear un objeto de la clase "Productos"
    def __init__(self, root):
        # Configuramos el objeto "root" (la ventana principal) para que sea el atributo "wind" de la clase "Productos"
        self.wind = root
        # Configuramos el título de la ventana
        self.wind.title("Productos")
        # Configuramos el tamaño de la ventana
        self.wind.geometry("850x600")
        # Creamos dos marcos (frames) para organizar la información del producto y los datos del producto
        frame1 = LabelFrame(self.wind, text= "Información del producto", font=("Calibri", 14))
        frame2 = LabelFrame(self.wind, text= "Datos del producto", font=("Calibri", 14))
        # Empaquetamos (packing) los marcos dentro de la ventana principal con cierto relleno y expansión
        frame1.pack(fill="both",expand="yes",padx=20, pady=10)
        frame2.pack(fill="both",expand="yes",padx=20, pady=10)

        self.trv = ttk.Treeview(frame1, columns = (1,2,3,4), show="headings", height="5")
        self.trv.pack()

        self.trv.heading(1, text="ID Del Producto")
        self.trv.heading(2, text="Nombre Del Producto")
        self.trv.heading(3, text="Precio Del Producto")
        self.trv.heading(4, text="Descripción Del Producto")
        #llamamos las funciones 
        self.consulta()

        #Función para la BD
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.base) as conn:  #La variable antes declarada
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
            return result
#Otra función para interactuar con la tabla 
    def consulta(self):
        book = self.trv.get_children() 
        for element in book:
            self.trv.delete(element)
        query = 'SELECT id, nombre, precio, descripcion FROM Productos'
        rows = self.run_query(query)
        for row in rows:
            self.trv.insert('', 0, text=row[1], values=row)

# Si este archivo está siendo ejecutado directamente por el intérprete de Python
if __name__ == '__main__':
    root = Tk() #Creamos una ventana principal (Tk) y la asignamos a la variable "root"
    product = Productos(root)
    # Creamos un objeto "Productos" y le pasamos la ventana principal como argumento
    root.mainloop() #Iniciamos el ciclo principal de eventos para la ventana
