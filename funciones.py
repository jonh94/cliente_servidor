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
def comparacion(n1,n2):
	if n1>n2:
		print("El mayor es n1: ",n1," ", n2)
	elif n2>n1:
		print("El mayor es : {},{}".format(n2,n1))
	else:
		print("Los numeros son iguales: {},{}".format(n1,n2))
#funcion para mostrar ciclo for
def cuenta(n1,n2):
	if (n2>n1):
		for i in range(n1,n2+1):
			print("Valor de i:{}".format(i))
	elif(n1>n2):
		for i in range(n1,n2-1,-1)):
			print("Valor de i:{}".format(i))
	else:
		print("los numeros son iguales: {},{}".format(n1,n2))
#inicia funcion principal

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
		b = int(input("ingrese el segundo numero:"))
		print("***** SELECCIONE UNA OPERACION ******")
		print("1.-SUMA")
		print("2.-RESTA")
		print("3.-DIVICION")
		print("4.-MULTIPLICACION")
		print("5.-NUMERO MAYOR")
		print("6.-NUMERACION")
		op = input("ingrese la operacion")

		#invocamos la operacion 
		if op == '1':
			print("la suma es: ", suma(a,b))
			print("El numero mayor es",(a,b))
		if op == '2':
			print("la resta es: ",resta(a,b))
			print("El numero mayor es",(a,b))
			
		if op == '4':
			print("el producto es: ",mult(a,b))
			print("El numero mayor es",(a,b))

		if op == '3':
			print("la divicion es: ",div(a,b))
			print("El numero mayor es",(a,b))
		if op == '5':
			print(comparacion(a,b))
		if op == '6':
			print(cuenta(a,b))

		#preguntamos por otra operacion
		ciclo = input("desea otra operacion(S/N)?")
	else:
		print("*** fin de programa ***")

if __name__ == "__main__":
	main()
