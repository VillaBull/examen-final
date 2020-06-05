from tkinter import *

master = Tk()

ancho = 600
alto = 400

master.geometry(str(ancho) + "x" + str(alto))
master.title("Examen Final")

Titulo = Label(text="BIENVENIDOS", font=("comic sans ms", 20)).place(x=200, y=5)

name=Label(text="Nombre", font=("Comic Sans ms", 14)).place(x=40, y=50)
ingreso=StringVar()
txt1=Entry(master, textvar="ingreso").place(x=125, y=60)
master.mainloop()