"""
Nombre : listas.py
Objetivo : muestra la funcion de las listas en python
Autor:
fecha 4 de agosto de 2020
"""

def main():
    lista = [1,23.01, False, "hola lista", 'A', [-1,-5], -12]

    listaVacia = []

    for elemento in lista:
        print("El elemento de la lista es: ", elemento)
    for i in listaVacia:
        print("el elemento de la lista es: ", i)

if __name__ == "__main__":
    main()