from tkinter import *
from datetime import date
from datetime import datetime


master = Tk()

ancho = 800
alto = 500

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
    fecha = f"{year.get()}-{month.get()}-{day.get()}"
    date_object = datetime.strptime(fecha, '%Y-%m-%d')

    today= datetime.today()
    
    c1 = today
    c2 = date_object
    result1 = abs(c1-c2).days 

    respuesta = f"Naciste el  {date_object} y has vivido {result1} días."

    lblresp.config(text=respuesta)

def contarLetras():

    fNombre = f"{nombre.get()}"
    fApellido = f"{apellido.get()}"

    conteo1 = len(fNombre)
    conteo2 = len(fApellido)
  

    if conteo1 % 2 == 0:
        x1 = f"{fNombre} el nombre ingresado es de numero par"
    else:
        x1 = f"{fNombre} El nombre ingresado es de numero impar"

    if conteo2 % 2 == 0:
        x2 = f"{fApellido} El Apellido ingresado es de numero Par."
    else:
        x2 = f"{fApellido} El Apellido ingresado es de número impar."

    respuesta = f"{x1} y  {x2} "

    lblresp.config(text= respuesta)

def bf():
    print("dia", bin(day.get())[2:], "mes", bin(month.get())[2:], "año", bin(year.get())[2:])
    respuesta = "la fecha en binario es: " + "dia", bin(day.get())[2:], "mes", bin(month.get())[2:], "año", bin(year.get())[2:]
    lblresp.config(text= respuesta)

def invertir_nombre():
    invirtiendo = nombre.get()+" "+apellido.get()
    invirtiendo = invirtiendo[::-1]
    respuesta = nombre.get() + " " + apellido.get() + " al revés es: "+ invirtiendo
    lblresp.config(text= respuesta)
    
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
txtDías = Entry(MyFrame, textvariable = day)
txtDías.grid(row=4, column=2)

Meses = Label(MyFrame, text = "Mes: ")
Meses.grid(row=5, column=1)
Meses.config(padx=5, pady=5)
txtMeses = Entry(MyFrame, textvariable = month)
txtMeses.grid(row=5, column=2)

Años = Label(MyFrame, text = "Año: ")
Años.grid(row=6, column=1)
Años.config(padx=5, pady=5)
txtAños = Entry(MyFrame, textvariable = year)
txtAños.grid(row=6, column=2)
    
btn1 = Button(MyFrame, text = "Función 1", command= bf)
btn1.grid(row = 7, column = 1)
btn1.config(padx=8, pady=8)

btn2 = Button(MyFrame, text = "Función 2", command = ContandoLosDías)
btn2.grid(row = 7, column = 2)
btn2.config(padx=8, pady=8)

btn3 = Button(MyFrame, text = "Función 3", command = contarLetras)
btn3.grid(row = 7, column = 3)
btn3.config(padx=8, pady=8)

btn4 = Button(MyFrame, text = "Función 4")
btn4.grid(row = 7, column = 4)
btn4.config(padx=8, pady=8)

btn5 = Button(MyFrame, text = "Función 5", command=invertir_nombre)
btn5.grid(row = 7, column = 5)
btn5.config(padx=8, pady=8)

lblresp = Label(MyFrame, text = "Acá saldrá la respuesta: ")
lblresp.grid(row=9, column = 0)
lblresp.config(padx=8, pady=8)

lblX=Label(MyFrame)
lblX.grid(row=10, column=0)
lblX.config(padx=10, pady=10)

master.mainloop()