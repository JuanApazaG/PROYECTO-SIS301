import tkinter as tk
from tkinter import*
from tkinter.font import BOLD
from tkinter import ttk,messagebox
import util.generic as utl
import forms.form_master as mas
import forms.form_inventario as reg





class registrar:

   # est es la funcion declarar 
   def declarar (self,registrar):
      self.usuario= IntVAr()
      self.costo= IntVAr()
      self.precio= IntVAr()
   
   def Menu1(self):
        self.ventana.destroy()
        mas.MasterPanel()

   def empleados1(self):
        self.ventana.destroy()
        reg.inventario()
        
        
   
  

   # la funcion eliminar tabla 
   def borrar (self):
    
      select_itre=self.tree.selection()
      self.tree.delete(select_itre)
      messagebox.showwarning(message="se elimino exitosamente",title="Mensaje2") 

   # funcioin agragar a tabla
   def agregar(self):
    
      usuario=self.usuario.get()
      costo=self.costo.get()
      precio=self.precio.get()
      
      
      self.tree.insert("",END,text=usuario,values=(costo,precio))

         
    # creacion de de la ventana 
   def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('registrar ')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h) )
        self.barraMenu=tk.Menu(self.ventana)
        self.ventana.config(bg='#2a8d90',menu=self.barraMenu)



        
        self.barraMenu.add_cascade(label="menu",command=self.Menu1)        
        self.barraMenu.add_cascade(label="registrar") 
        self.barraMenu.add_cascade(label="empleados",command=self.empleados1) 
        self.barraMenu.add_cascade(label="informe") 
        

        # marco logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='#2a8d90')
        frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)

     
        
        

        # creacion de la taba  
        self.tree=ttk.Treeview(frame_logo)
        self.tree.grid(row=4,column=0,sticky='ns',columnspan=4)

        self.barra=Scrollbar(frame_logo,command=self.tree.yview_scroll)
    
        self.tree.config(yscrollcommand=self.barra)

        
        
        
         
        self.tree['columns']=('NOMBRE','COSTO',)
        #self.tree.column('#0',width=0,stretch=NO) 
      
        # configuracion de la tabla
          
        self.tree.heading('#0',text='NOMBRE',anchor='n')  
        self.tree.heading('NOMBRE',text='CANTIDAD',anchor='n')   
        self.tree.heading('COSTO',text='COSTO',anchor='n') 
        self.tree.place(x=13,y= 140) 
       
        logo2 =utl.leer_imagen("./imagenes/logo6.png", (200, 200))
        label = tk.Label( frame_logo, image=logo2,bg='#2a8d90' )
        label.place(x=13,y=590)
        
       

        #marco de los botones          
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#2a8d90')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #
       

        #marco de titulo 
        frame_form_top = tk.Frame(frame_form,height = 0, bd=0, relief=tk.SOLID,bg='#2a8d90')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="EL FOGON CHAQUEÑO ",font=('Times', 30,BOLD,), fg="red",bg='#2a8d90',pady=30)
        title.pack(expand=tk.YES,fill=tk.BOTH)

        title2 = tk.Label(frame_form_top, text=" REGISTRO DE PRODUCTOS  ",font=('Times', 24,), fg="blue",bg='#2a8d90',pady=1)
        title2.pack(expand=tk.YES,fill=tk.BOTH)

        # label de nombres 
        etiqueta_usuario = tk.Label(frame_form, text="NOMBRE PRODUCTO", font=('Times', 22,BOLD) ,fg="BLACK",bg='#2a8d90', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        # casa para escribir 
        self.usuario = tk.Entry(frame_form, font=('Times', 18))
        self.usuario.pack(fill=tk.X, padx=20,pady=0)

        etiqueta_precio = tk.Label(frame_form, text="CANTIDAD", font=('Times', 22,BOLD) ,fg="BLACK",bg='#2a8d90', anchor="w")
        etiqueta_precio.pack(fill=tk.X, padx=20,pady=5)
        self.precio = tk.Entry(frame_form, font=('Times', 18))
        self.precio.pack(fill=tk.X, padx=20,pady=0)
        
        etiqueta_costo = tk.Label(frame_form, text="COSTO   (en bs)", font=('Times', 22,BOLD) ,fg="BLACK",bg='#2a8d90', anchor="w")
        etiqueta_costo.pack(fill=tk.X, padx=10,pady=5)
        self.costo = tk.Entry(frame_form, font=('Times', 18))
        self.costo.pack(fill=tk.BOTH, padx=20,pady=0)


        # botom registrar 
        insertar = tk.Button(frame_form,text="registrar ",command=self.agregar,font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff")
        insertar.pack( padx=20,pady=10)  
        #boton eliminar    
        eliminar = tk.Button(frame_form,text="eliminar",command=self.borrar,font=('Times', 15,BOLD),bg='#FA0000', bd=0,fg="#fff")
        eliminar.pack( padx=0,pady=0) 
       

      

        self.ventana.mainloop()