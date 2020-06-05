from tkinter import *
from datetime import date
from datetime import datetime


master = Tk()

ancho = 600
alto = 400

master.geometry(str(ancho) + "x" + str(alto))
master.title("Examen Final")

MyFrame=Frame()
MyFrame.pack()
Titulo = Label(MyFrame, text="Bienvenido")
Titulo.grid(row=1, column=1)
Titulo.config(font=("comic sans ms",20))

abc = StringVar()
ingreso = StringVar()
xyz = IntVar()
pqr = IntVar()
out = IntVar()











name = Label(text="Nombre", font=("Comic Sans ms", 14)).place(x=100, y=50)
txt1 = Entry(master, textvar="abc").place(x=175, y=60)

apellido = Label(text="Apellido",font = ("comic sans ms", 14)).place(x = 100, y = 80)
txt2 = Entry(master, textvar = "ingreso").place(x = 175, y = 90)

Día = Label(text="    Día  ",font = ("comic sans ms", 14)).place(x = 100, y = 110)
txt3 = Entry(master, textvar = "xyz").place(x = 175, y = 120)

Mes = Label(text="   Mes  ",font = ("comic sans ms", 14)).place(x = 100, y = 140)
txt4 = Entry(master, textvar = "pqr").place(x = 175, y = 150)

Año = Label(text="   Año  ",font = ("comic sans ms", 14)).place(x = 100, y = 170)
txt5 = Entry(master, textvar = "out").place(x = 175, y = 180)




btn1 = Button(master, text = "Función 1", font = ("Comic Sans ms", 10), width=8).place(x=20, y=210)

btn2 = Button(master, text = "Función 2", font = ("Comic Sans ms", 10), width=8).place(x=95, y=210)

btn3 = Button(master, text = "Función 3", font = ("Comic Sans ms", 10), width=8).place(x=170, y=210)

btn4 = Button(master, text = "Función 4", font = ("Comic Sans ms", 10), width=8).place(x=245, y=210)

btn5 = Button(master, text = "Función 5", font = ("Comic Sans ms", 10), width=8).place(x=320, y=210)

master.mainloop()