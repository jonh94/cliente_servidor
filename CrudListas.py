"""
Nombre: CrudListas.py
Objetivo: implementa las funciones cruden una lista en python
autor:
fecha: 4 de agoasto de 2020
"""
# funcion para agregar elementos a la lista
def agregarELemento():
    return

# funcion para buscar elementos en la lista
def getElement():
    return

# funcion para modificar elementos en la lista
def modifyElement():
    return

# funcio para eliminara elementos en la lista 
def delElement():
    return

def dashboar():
     print("== Operaciones crud con lista en pythn == ")
     print("1.- Agregar elementos")
     print("2.- Buscar elementos")
     print("3.- Cambiar elementos ")
     print("4.- Eliminar elementos")
     print("5.- Salir")
def main():
    ciclio = 'S'
    while ciclio == 'S' or ciclio == 's':
        dashboar()
        ciclio = input("Seleccione una opcion entre 1 y 5 ")
    else:
        print("*** Fin de programa ***")

if __name__ == "__main__":
    main()