import tkinter as tk
from tkinter import*
from tkinter import filedialog
from tkinter.font import BOLD
from tkinter import ttk,messagebox
import util.generic as utl
import forms.form_master as mas
import forms.form_registrar as reg




class inventario:

   def menu1 (self):
      self.ventana.destroy()
      mas.MasterPanel()
   

   def registrar1 (self):
      self.ventana.destroy()
      mas.registrar()

   def eliminar_empleados(self):
      select_itre=self.tree.selection()
      self.tree.delete(select_itre)
      messagebox.showwarning(message="se elimino exitosamente",title="Mensaje2")
   

   def guardar(self):
    
      ci=self.ci.get()
      nombre=self.nombre.get()
      apellido_p=self.apellido_p.get()
      apellido_m=self.apellido_m.get()
      telefono=self.telefono.get()
      cargo=self.cargo.get()
      direcion=self.direcion.get()
      
      
      self.tree.insert("",END,text=ci,values=(nombre,apellido_p,apellido_m,telefono,cargo,direcion))
      

   
   
   
   

   def ventanarefistro(self):
      self.ventana_R = tk.Tk()                             
      self.ventana_R.title('Inicio de sesion')
      self.ventana_R.geometry('390x540')
      utl.centrar_ventana(self.ventana_R,390,540)
     


      
      





      self.marco=tk.LabelFrame(self.ventana_R,text="DATOS PERSONALES",font=("Comic Sans",10,"bold"))
      self.marco.config(bd=2)
      self.marco.pack()
   


      ci = tk.Label(self.marco, text="CI", font=('Comic Sans', 10,BOLD) ,fg="BLACK",bg='#fcfcfc', anchor="w").grid(row=0,column=0,padx=5,pady=10)
      # casa para escribir 
      self.ci= tk.Entry(self.marco, width=25)
      self.ci.grid(row=0,column=1,padx=5,pady=10)

      nombre = tk.Label(self.marco, text="NOMBRE", font=('Comic Sans', 10,BOLD) ,fg="BLACK",bg='#fcfcfc', anchor="w").grid(row=1,column=0,padx=10,pady=10)
      # casa para escribir 
      self.nombre = tk.Entry(self.marco, width=25)
      self.nombre.grid(row=1,column=1,padx=10,pady=10)


      apellido_p = tk.Label(self.marco, text="APELLIDO.P", font=('Comic Sans', 10,BOLD) ,fg="BLACK",bg='#fcfcfc', anchor="w").grid(row=2,column=0,padx=15,pady=10)
      # casa para escribir 
      self.apellido_p = tk.Entry(self.marco, width=25)
      self.apellido_p.grid(row=2,column=1,padx=15,pady=10)


      apellido_m = tk.Label(self.marco, text="APELLIDO.M", font=('Comic Sans', 10,BOLD) ,fg="BLACK",bg='#fcfcfc', anchor="w").grid(row=3,column=0,padx=20,pady=10)
      # casa para escribir 
      self.apellido_m = tk.Entry(self.marco, width=25)
      self.apellido_m.grid(row=3,column=1,padx=20,pady=10)

      telefono = tk.Label(self.marco, text="TELEFONO", font=('Comic Sans', 10,BOLD) ,fg="BLACK",bg='#fcfcfc', anchor="w").grid(row=4,column=0,padx=25,pady=10)
      # casa para escribir 
      self.telefono = tk.Entry(self.marco, width=25)
      self.telefono.grid(row=4,column=1,padx=25,pady=10)


      cargo = tk.Label(self.marco, text="CARGO", font=('Comic Sans', 10,BOLD) ,fg="BLACK",bg='#fcfcfc', anchor="w").grid(row=5,column=0,padx=30,pady=10)
      # casa para escribir 
      self.cargo = tk.Entry(self.marco, width=25)
      self.cargo.grid(row=5,column=1,padx=30,pady=10)

      
      direcion = tk.Label(self.marco, text="DIRECION", font=('Comic Sans', 10,BOLD) ,fg="BLACK",bg='#fcfcfc', anchor="w").grid(row=6,column=0,padx=35,pady=10)
      # casa para escribir 
      self.direcion = tk.Entry(self.marco, width=25)
      self.direcion.grid(row=6,column=1,padx=35,pady=10)



      # botom guardar 
      guardar = tk.Button(self.ventana_R,text="guardar ",command=self.guardar,font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff")
      guardar.pack( padx=4,pady=100)



      
    








   def __init__(self):        
     

      self.ventana = tk.Tk()                             
      self.ventana.title('registrar ')
      w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
      self.ventana.geometry("%dx%d+0+0" % (w, h) )
      self.barraMenu=tk.Menu(self.ventana)
      self.ventana.config(bg='#2a8d90',menu=self.barraMenu)

      self.barraMenu.add_cascade(label="menu",command=self.menu1)        
      self.barraMenu.add_cascade(label="imventario",command=self.registrar1) 
      self.barraMenu.add_cascade(label="empleados") 
      self.barraMenu.add_cascade(label="informe") 



      title = tk.Label(self.ventana, text="REGISTRO DE PERSONAL",font=('Times', 30,BOLD,), fg="red",bg='#2a8d90',pady=30)
      title.grid(row=3,column=0,padx=450,pady=10)


      logo3 =utl.leer_imagen("./imagenes/logo9.png", (200, 200))
      label = tk.Label( self.ventana, image=logo3,bg='#2a8d90' )
      label.place(x=600,y= 80)

    


      self.tree=ttk.Treeview(self.ventana)
      self.tree.grid(row=4,column=0,sticky='ns',columnspan=4)

      self.barra=Scrollbar(self.ventana,command=self.tree.yview_scroll)
    
      self.tree.config(yscrollcommand=self.barra)

        
        
        
         
      self.tree['columns']=('NOMBRE','APELLIDO.P','APELLIDO.M','TELEFONO','CARGO','DIRECION')
        #self.tree.column('#0',width=0,stretch=NO) 
      
        # configuracion de la tabla
          
      self.tree.heading('#0',text='CI',anchor='n')  
      self.tree.heading('NOMBRE',text='NOMBRE',anchor='n')   
      self.tree.heading('APELLIDO.P',text='APELLIDO.P',anchor='n') 
      self.tree.heading('APELLIDO.M',text='APELLIDO.M',anchor='n') 
      self.tree.heading('TELEFONO',text='TELEFONO',anchor='n')
      self.tree.heading('CARGO',text='CARGO',anchor='n')
      self.tree.heading('DIRECION',text='DIRECION',anchor='n')
      self.tree.place(x=50,y= 275) 
      
      
      # botom registrar 
      insertar = tk.Button(self.ventana,text="registrar ",command=self.ventanarefistro,font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff")
      insertar.place( x=700,y=550) 
      

      eliminar = tk.Button(self.ventana,text="eliminar",command=self.eliminar_empleados,font=('Times', 15,BOLD),bg='#FA0000', bd=0,fg="#fff")
      eliminar.place( x=600,y=550)

      logo2 =utl.leer_imagen("./imagenes/logo6.png", (200, 200))
      label = tk.Label( self.ventana, image=logo2,bg='#2a8d90' )
      label.place(x=13,y=590)


      logo4 =utl.leer_imagen("./imagenes/logo10.png", (220, 220))
      label = tk.Label( self.ventana, image=logo4,bg='#2a8d90' )
      label.place(x=1200,y=590)



    




      
      
       



      self.ventana.mainloop()