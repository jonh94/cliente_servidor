"""
Nombre: Circunferencia.py
Objetivo: permite calcular el area de una cricunferencia 
Autor:
Fecha: 28 de julio de 2020
"""
# importamos la libreria math
import math

#Funciom para calcular area 
def calcularAre(valorRadio):
	return math.pi*math.pow(valorRadio,2)

#Modulo principal
def main():
	ciclo ='S'
	while ciclo == 'S' or ciclo == 's':
		print("--- programa para calcular area de circunferencia ---")
		vradio = int(input("introduce el valor del radio."))
		print("el area de la circunferncia con radio igual a: {}, es: {}".format(vradio,calcularAre(vradio)))
		ciclo = input("Otro calculo?(s/n)")
	else:
		print("fin de progrma")
if __name__ == "__main__":
	main()
