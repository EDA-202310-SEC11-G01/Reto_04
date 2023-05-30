﻿"""
* Copyright 2020, Departamento de sistemas y Computación,
* Universidad de Los Andes
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
import model
import time
from datetime import datetime
import csv
import tracemalloc
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import quicksort as quk
from DISClib.ADT import graph as gr
csv.field_size_limit(2147483647)


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""




def new_controller():
   """
   Crea una instancia del modelo
   """
   #TODO: Llamar la función del modelo que crea las estructuras de datos
   return model.new_data_structs()




# Funciones para la carga de datos




# Funciones de ordenamiento


# Funciones de consulta sobre el catálogo


def get_data(control, id):
   """
   Retorna un dato por su ID.
   """
   #TODO: Llamar la función del modelo para obtener un dato
   pass




def req_1(control):
   """
   Retorna el resultado del requerimiento 1
   """
   # TODO: Modificar el requerimiento 1
   return model.req_1(control)




def req_2(control):
   """
   Retorna el resultado del requerimiento 2
   """
   # TODO: Modificar el requerimiento 2
   pass




def req_3(control, wolf_list):
   """
   Retorna el resultado del requerimiento 3
   """
   return model.req_3(control, wolf_list)
   




def req_4(control):
   """
   Retorna el resultado del requerimiento 4
   """
   # TODO: Modificar el requerimiento 4
   pass




def req_5(control):
   """
   Retorna el resultado del requerimiento 5
   """
   # TODO: Modificar el requerimiento 5
   pass


def req_6(control):
   """
   Retorna el resultado del requerimiento 6
   """
   # TODO: Modificar el requerimiento 6
   pass




def req_7(control):
   """
   Retorna el resultado del requerimiento 7
   """
   # TODO: Modificar el requerimiento 7
   pass




def req_8(control):
   """
   Retorna el resultado del requerimiento 8
   """
   # TODO: Modificar el requerimiento 8
   pass




# Funciones para medir tiempos de ejecucion


def get_time():
   """
   devuelve el instante tiempo de procesamiento en milisegundos
   """
   return float(time.perf_counter()*1000)




def delta_time(start, end):
   """
   devuelve la diferencia entre tiempos de procesamiento muestreados
   """
   elapsed = float(end - start)
   return elapsed


def get_memory():
   """
   toma una muestra de la memoria alocada en instante de tiempo
   """
   return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
   """
   calcula la diferencia en memoria alocada del programa entre dos
   instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
   """
   memory_diff = stop_memory.compare_to(start_memory, "filename")
   delta_memory = 0.0


   # suma de las diferencias en uso de memoria
   for stat in memory_diff:
       delta_memory = delta_memory + stat.size_diff
   # de Byte -> kByte
   delta_memory = delta_memory/1024.0
   return delta_memory
