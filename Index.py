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

nombre = StringVar()
apellido = StringVar()
day = IntVar()
month = IntVar()
year = IntVar()

def ContandoLosDías():
    StrFecha = f"{year.get()}-{month.get()}-{day.get()}"
    date_object = datetime.strptime(StrFecha, '%Y-%m-%d')
    today = datetime.today()

    x1 = today
    x2 = date_object
    respuesta1 = abs(x1-x2).days

    respuesta1 = f"tu fecha de nacimiento es{date_object} y ha vivido {respuesta1}"

    lblresp.configure(Text = respuesta1)

    def ContandoLasLetras():
        Nombre = f"{nombre.get()}"
        Apellido = f"{apellido.get()}"

        contar1 = len(nombre)
        contar2 = len(apellido)

        if contar1 % 2 == 0:
            a1 = f"{nombre}el nombre ingresado es de numero par"
        else:
            a1 = f"{nombre}el nombre ingresado es de numero impar"


        if contar2 % 2 == 0:
             a2 = f"{apellido}el apellido ingresado es de numero par"
        else:
             a2 = f"{apellido} el apellido ingresado es de numero impar"

        respuesta2 = f"{a1} y {a2}"

        lblresp.configure(text = respuesta2)

nombres = Label(MyFrame, text = "Nombre: ")
nombres.grid(row=2, column=1)
nombres.config(padx=5, pady=5)
txtnombres = Entry(MyFrame, textvariable = nombre)
txtnombres.grid(row=2, column=2)

Apellidos = Label(MyFrame, text = "Apellido: ")
Apellidos.grid(row=3, column=1)
Apellidos.config(padx=10, pady=10)
txtApellido = Entry(MyFrame, textvariable = apellido)
txtApellido.grid(row=3, column=2)

Días = Label(MyFrame, text = "Día: ")
Días.grid(row=4, column=1)
Días.config(padx=5, pady=5)
txtDías = Entry(MyFrame, textvariable = nombre)
txtDías.grid(row=4, column=2)

Meses = Label(MyFrame, text = "Mes: ")
Meses.grid(row=5, column=1)
Meses.config(padx=5, pady=5)
txtMeses = Entry(MyFrame, textvariable = nombre)
txtMeses.grid(row=5, column=2)

Años = Label(MyFrame, text = "Año: ")
Años.grid(row=6, column=1)
Años.config(padx=5, pady=5)
txtAños = Entry(MyFrame, textvariable = nombre)
txtAños.grid(row=6, column=2)

btn1 = Button(MyFrame, text = "Función 1")
btn1.grid(row = 7, column = 0)
btn1.config(padx=8, pady=8)


    
master.mainloop()