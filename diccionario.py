"""
Nombre: Diccionario.py
Objetivo : muestra la operacion de los diccionarios en python
Autor: 
fecha: 5 de agosto de 2020
"""

# un diccionario es una estructua de datos que alamacena valores hetereogeneos
#pero los almacena en un formato de clarve valor: quiere decirque cada elemento 
#en el diccionario se almacena como una lista de pares key: valo.
#por ejemplo: 'nombre':'Francisco Cervantes Zambrano'
#no son mutables
#con los mismos valores, no podremos introducir mas datos 
def main():
    dic = {'clave':20082133, 'nombre':'Erick Jose Verduzco Campos', 'edad':54, 'cursos':['python','prog web', 'inteligencia artificial']}
    print("los items son",dic)

    print("El valor de la key es:", dic['nombre'], "\n")

    for i in dic:
        print(i,":",dic[i])

    for i in dic['cursos']:
        print(i)





if __name__ == "__main__":
    main()