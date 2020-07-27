"""
Nombre: funciones.py
Objetivo: muestra la operacion de las funciones en python
Autor:
Fecha: 27 julio de 2020
"""

def mensaje():
	print("hola desde mensaje")

def regresamensaje():
	return "saludo desde regresamensaje"

def printmensaje(msg):
	print(msg)
def suma(n1,n2):
	return n1+n2
#Tarea: agregar las tres funciones restantes y subir a github la carpeta en modo terminal
def resta(n1,n2):
	return n1-n2
def mult(n1,n2):
	return n1*n2
def div(n1,n2):
	return n1/n2

def main():
	ciclo = 'S'
	while ciclo == 'S' or ciclo =='s':
		#invocamos funcion mensaje
		mensaje()
		#invocarmos funcion regresamensaje
		print(regresamensaje())
		#invocamos printmensaje
		printmensaje("hola te saludo...")
		#leer datos por teclado
		a = int(input("ingrese el pimer numero:"))
		op = input("operacion: ")
		b = int(input("ingrese el segundo numero:"))
		#invocamos la funcion suma 
		if op == '+':
			print("la suma es: ", suma(a,b))
		if op == '-':
			print("la resta es: ",resta(a,b))
		if op == '*':
			print("el producto es: ",mult(a,b))
		if op == '/':
			print("la divicion es: ",div(a,b))
		#preguntamos por otra operacion
		ciclo = input("desea otra operacion(S/N)?")
	else:
		print("*** fin de programa ***")

if __name__ == "__main__":
	main()
