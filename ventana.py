"""
Nombre: ventana.py
Objetivo: mostrar como trabajar con ventanas gui en python con tkinter
Autor:
Fecha: 29 de julio de 2020

"""
#importamos las librerias de tkinter
from tkinter import *
from tkinter import ttk 

#funcion para enviar datos al servidor echo
def sendToServer():
	
	print("Enviado....")

#Funcion principal
def main():
	#creamos ventana contenedora 
	win = Tk()
	#Modificamos parametros de la ventana 
	win.geometry("400x400")
	win.title("mi primer ventana en tkinter")
	#Crear etiqueta 
	label = ttk.Label(win, text="Texto a enviar al servidor").pack(side=TOP)
	textCampo = ttk.Entry(win).pack(side=TOP)
	#Creamos boton para enviar texto al servidor
	ttk.Button(win, text="Enviar", command=sendToServer).pack(side=BOTTOM)
	#creamos boton en ventana y lo colocamos en la ventana 
	ttk.Button(win, text="Salir", command=quit).pack(side=BOTTOM)
	#Hacemos un ciclo para dibujar y esperar eventos 
	win.mainloop()

if __name__ == "__main__":
	main()
