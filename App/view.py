"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
default_limit = 1000 
sys.setrecursionlimit(default_limit*100000)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    return controller.new_controller()

def tabulate_data(data_set,header):
    data_set_org=[]
    for i in data_set:
        i=dict([(key,val) for key,val in i.items() if key in header])
        data_set_org.append(i)
    rows=[x.values() for x in data_set_org]
    print(tabulate(rows,list(data_set_org[0].keys()),tablefmt='grid',stralign='center',maxheadercolwidths=13,maxcolwidths=13))

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    '''
    Todo esta ya hecho falta el print del view osea las palabras y eso pero la info esta alli, osea todo esta hecho solo falta mostrarlo. Esto del view 
    usualemnte lo hacemos al final del reto siempre , porque es la parte menos importante, entonces eimpre lo dejamos hasta el final, todo lo del view.
    '''
    a=controller.load_data(control)
    print("Total de lobos reconocidos en el estudio:", a[1])
    print("Total de eventos cargados durante el estudio:", a[2])
    print("Total de puntos de encuentro reconocidos:", a[3])
    print("Total de puntos de seguimiento reconocidos:", a[4])
    print("Total de arcos creados para unir los nodos de encuentro y los puntos de seguimiento:", a[5])
    print("Total de arcos creados para representar el movimiento de los individuos:", a[6])
    print("Rango del área rectangular que ocupan los lobos grises de Boutin Alberta en Canadá:")
    print("Latitud mínima & máxima:", str(a[7][0][0])+' and '+str(a[7][0][1]))
    print("Longitud mínima & máxima:", str(a[7][1][0])+' and '+str(a[7][1][1]))
    print('\n')
    print('\n')
    headers=["Identificador del punto de encuentro","Geolocalización","Total de lobos","Lista de identificadores"]
    print(tabulate(a[8]['elements'],headers,tablefmt='grid',stralign='center',maxheadercolwidths=15,maxcolwidths=15))
    
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print(controller.req_1(control))

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    # Solicitar localización geográfica del punto de origen
    origen = tuple(float(coord[1:-1]) for coord in input("Ingrese la latitud y longitud del punto de origen de la forma (lon,lat): ").split(','))

    # Solicitar localización geográfica del punto de destino

    destino = tuple(float(coord[1:-1]) for coord in input("Ingrese la latitud y longitud del punto de destino (lon,lat): ").split(','))

    print(controller.req_4(control,origen,destino))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print(controller.req_6(control,'2013-02-16 00:00','2014-10-23 23:59','hembras'))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print(controller.req_7(control,'2012-11-28 00:00','2014-05-17 23:59','-17.3','9.7'))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                data = load_data(control)
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
