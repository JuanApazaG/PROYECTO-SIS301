import tkinter as tk
from tkinter import*
from tkinter.font import BOLD
import util.generic as utl
from forms.form_registrar import registrar
import forms.form_inventario as inven

class MasterPanel:
    
    def inventario(self):
      self.ventana.destroy()
      inven.inventario()

    def registrar (self):
        self.ventana.destroy()
        registrar()
    

   
                                      
    def __init__(self):        
        
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.barraMenu=tk.Menu(self.ventana)
        self.ventana.config(bg='BLACK',menu=self.barraMenu)  

       
        self.barraMenu.add_cascade(label="menu",)        
        self.barraMenu.add_cascade(label="regitrar",command=self.registrar) 
        self.barraMenu.add_cascade(label="Empleados",command=self.inventario) 
        self.barraMenu.add_cascade(label="informe") 
        
       
        
         

      


        logo =PhotoImage(file="./imagenes/logo6.png")
        
           
        label = tk.Label( self.ventana, image=logo,bg='BLACK' )
        label.place(x=0,y=0,relwidth=1,relheight=1)



        logo1 =utl.leer_imagen("./imagenes/logo4.png", (300, 300))
        label = tk.Label( self.ventana, image=logo1,bg='BLACK' )
        label.place(x=10,y=20)
       

        logo2 =utl.leer_imagen("./imagenes/logo13.png", (300, 300))
        label = tk.Label( self.ventana, image=logo2,bg='BLACK' )
        label.place(x=1150,y=20)

        logo3 =utl.leer_imagen("./imagenes/logo7.png", (300, 300))
        label = tk.Label( self.ventana, image=logo3,bg='BLACK' )
        label.place(x=10,y=510)
        


        logo4 =utl.leer_imagen("./imagenes/logo8.png", (300, 300))
        label = tk.Label( self.ventana, image=logo4,bg='BLACK' )
        label.place(x=1150,y=510)

        
             

        self.ventana.mainloop()