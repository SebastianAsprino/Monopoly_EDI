import pygame
import tkinter as tk
from tkinter import ttk

# funcion de cuand se oprime el boton
def push():
    #aqui se deberia anexar el nombre de cada jugador, y su turno
    acceso = cajon.get()
    condicion=acceso
    numjugadores.destroy()
    if condicion == '2':
        print("2 jugadores")
    elif condicion == '3':
        print("3 jugadores")
    elif condicion == '4':
        print("4 jugadores")

# crea la ventana para saber el numero de jugadores
numjugadores = tk.Tk()
# estos son los parametros de la ventana principal
# titulo de la ventana
numjugadores.title('Jugadores')
# tamaño y color
numjugadores.config(width=350,height=106,background='#CBE8E0')
# iconos
numjugadores.iconbitmap("assets\logo.ico")
# texto de laventana
etiqueta= ttk.Label(text="Numero De Jugadores: ",background='#CBE8E0')
etiqueta.place(x=18, y=20)
# la caja de seleccion del numero de jugadores
cajonstyle = ttk.Style()
cajonstyle.theme_create('combostyle', parent='alt', settings = {'TCombobox':{'configure':{'selectbackground': '#CBE8E0', 'fieldbackground': '#CBE8E0','background': '#CBE8E0'}}})
cajonstyle.theme_use('combostyle') 
cajon = ttk.Combobox(state="readonly",values=['2', '3', '4'])
cajon.place(x=140, y=20)
# esta parte se encarga de crear el boton de la seleccion de jugadores
boton = ttk.Button(text="  ▶  ", command=push )
boton.place(x=290, y=20)

numjugadores.resizable(False, False)
numjugadores.mainloop()
# llama todos los modulos de pygame
pygame.init()
class tablero:
    """esta clase crea el visual del tablero"""
    