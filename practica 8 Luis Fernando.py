import os

lista = []
import os

lista = []


# subprograma
def crearArchivo():
    empleados = open("datosEmpleados.txt", "w")
    print("El archivo ha sido creado")
    empleados.close()


def ingresarempleados():
    nombreEmpleado = input("Digite el nombre el nombre del empleado:")
    lista.append(nombreEmpleado)
    empleados = open("DatosEmpleados.txt", "a")
    empleados.write(nombreEmpleado+ "\n")
    print("Los nombres de los empleados fueron guardado correctamente")
    empleados.close()
def consultarempleados():
    g = input("Digite el nombre del empleado") in lista
    print(g)

def modificarempleados():
        for x in range(len(lista)):
            print(lista[x])

        l = input("Digite el nombre del empleado que desea modificar")
        lista.remove(l)
        k = input("Digite el nuevo nombre del empleado que desea")
        lista.append(k)
def eliminarempleados():
    for x in range(len(lista)):
        print(lista(x))


    w = input("Digite el nombre de la persona que desea eliminar de la lista")
    lista.pop(w)
def imprimirlosempleados():
        empleados = open("datosEmpleados.txt", "r")
        datos = empleados.read()
        print(datos)
        empleados.close()

def main():
    while True:
        print("\t\t\t Menu Principal \t\t\t")
        print("1- ingresar empleados")
        print("2-consultar si un empleado existe")
        print("3-modificar empleados")
        print("4-Eliminar empleados")
        print("5-imprimir los empleados del archivo")
        print("6-salir")

        x = int(input("Digite el numero que desea ingresar"))

        if x == 1:
            ingresarempleados()

        elif x == 2:
            consultarempleados()

        elif x == 3:
            modificarempleados()

        elif x == 4:
            eliminarempleados()

        elif x == 5:
            imprimirlosempleados()

        elif x == 6:
            break
        else:
            print("Ningun dato es correcto intente nuevamente")


main()
