import tkinter as tk

#create a new instance - class Th()

mywindow = tk.Tk()

#Let's create a title and some text

mywindow.title("Python + Tkinter GUI")
mywindow.geometry("600x400")
mywindow.resizable(False,False)

mywindow.config(background = "#2798FA")
main_title = tk.Label (text = "Tkinter GUI - Truzz Blogg", font = ("Tahoma", 14), bg = "#ff7763", fg = "black", width = "60", height = "4")
main_title.place(x = 0, y = 50)

#let's launch the application - preveting closing using mainloop method)

mywindow.mainloop()

class juan:
    hola = 1
   