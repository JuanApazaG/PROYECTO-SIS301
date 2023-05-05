import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    

   
                                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#CDCDB7')
        self.ventana.resizable(width=0, height=0)            
        
        logo =utl.leer_imagen("./imagenes/logo4.png", (500, 500))
        
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='#CDCDB7')
        frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)    
        label = tk.Label( self.ventana, image=logo,bg='#fcfcfc' )
        label.place(x=-380,y=0,relwidth=1, relheight=1)
        
        
        #
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_form
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 0, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text=" CHURASQUERIA VICTOR'S ",font=('Times', 30), fg="red",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        
        
             

        self.ventana.mainloop()