from tkinter import *

master = Tk()

ancho = 600
alto = 400

master.geometry(str(ancho) + "x" + str(alto))
master.title("Examen Final")

Titulo = Label(text="BIENVENIDOS", font=("comic sans ms", 20)).place(x=200, y=5)

name = Label(text="Nombre", font=("Comic Sans ms", 14)).place(x=40, y=50)
ingreso = StringVar()
txt1 = Entry(master, textvar="ingreso").place(x=125, y=60)

apellido = Label(text="Apellido",font = ("comic sans ms", 14)).place(x = 40, y = 80)
ingreso = StringVar()
txt2 = Entry(master, textvar = "ingreso").place(x = 125, y = 90)

Día = Label(text="    Día  ",font = ("comic sans ms", 14)).place(x = 40, y = 110)
ingreso = StringVar()
txt3 = Entry(master, textvar = "ingreso").place(x = 125, y = 120)

Mes = Label(text="   Mes  ",font = ("comic sans ms", 14)).place(x = 40, y = 140)
ingreso = StringVar()
txt4 = Entry(master, textvar = "ingreso").place(x = 125, y = 150)

Año = Label(text="   Año  ",font = ("comic sans ms", 14)).place(x = 40, y = 170)
ingreso = StringVar()
txt5 = Entry(master, textvar = "ingreso").place(x = 125, y = 180)

master.mainloop()