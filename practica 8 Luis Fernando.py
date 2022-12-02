import os
lista=[]
#subprograma
def crearArchivo():
    compras=open("datosEmpleados.txt","w")
    print("El archivo ha sido creado")
    compras.close()
def ingresarempleados():
    nombreEmpleado=input("Digite el nombre del producto que desee comprar:")
    compras=open("DatosEmpleados.txt","a")
    compras.write(nombreEmpleado"\n")
    print("Los nombres de los empleados fueron guardado correctamente")
    compras.close()

def consultarempleados():


def modificarempleados():

def eliminarempleados():


def imprimirlosempleados():
#Menu principal
def main():
    while True:
        print("\t\t\t Menu Principal \t\t\t")
        print("1- ingresar empleados")
        print("2-consultar si un empleado existe")
        print("3-modificar empleados")
        print("4-Eliminar empleados")
        print("5-imprimir los empleados del archivo")
        print("6-salir")

        x=int(input("Digite el numero que desea ingresar"))

        if x==1:
            ingresarempleados():

        elif x==2:
            consultarempleados():

        elif x==3:
            modificarempleados():

        elif x==4:
            eliminarempleados()

        elif x==5:
            imprimirlosempleados()

        elif x==6
            break
        else:
            print("Ningun dato es correcto intente nuevamente")

main()
