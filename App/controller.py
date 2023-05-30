"""
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


def load_data(control):
   """
   Carga los datos del reto
   """
   # TODO: Realizar la carga de datos
   raw_data_2=csv.DictReader(open("Data/wolfs/BA-Grey-Wolf-individuals-utf8-large.csv", encoding = "utf-8"), delimiter= ",")
   list_individual_wolfs=lt.newList(datastructure='ARRAY_LIST')
   for l in raw_data_2:
      l['individual-id']=l['animal-id']+'_'+l['tag-id']
      lt.addLast(list_individual_wolfs,l)

   raw_data = csv.DictReader(open("Data/wolfs/BA-Grey-Wolf-tracks-utf8-small.csv", encoding = "utf-8"), delimiter= ",")
   hash_table_per_wolf=mp.newMap(numelements=45,loadfactor=0.75,maptype='PROBING') 
   hiper_nodes=mp.newMap(numelements=45,loadfactor=0.75,maptype='PROBING')
   hiper_nodes_list=mp.newMap(numelements=45,loadfactor=0.75,maptype='PROBING')
   array_vertex=lt.newList(datastructure='ARRAY_LIST')
   five_first_last=lt.newList(datastructure='ARRAY_LIST')
   hash_vertex=mp.newMap(numelements=45,loadfactor=0.75,maptype='PROBING')

   counter_wolfs=0
   for line in raw_data:
      line['time_datetime']=datetime.strptime(line['timestamp'],'%Y-%m-%d %H:%M')
      line['lon_lat']=(round(float(line['location-long']),3),round(float(line['location-lat']),3))
      line['individual-id']=line['individual-local-identifier']+'_'+line['tag-local-identifier']

      line['vertex']=str(str(str(line['lon_lat'][0])+'_'+str(line['lon_lat'][1])+'_'+line['individual-id']).replace('.','p').replace('-','m'))
      model.add_data(hash_table_per_wolf,line)
      model.add_data_hiper_nodes(hiper_nodes,line)
      counter_wolfs+=1

   counter_follow_nodes=0        
   for wolf in lt.iterator(hash_table_per_wolf['table']):
      if wolf['key']!=None:
         wolf['value']=quk.sort(wolf['value'],model.cmp_time)
         for j in lt.iterator(wolf['value']):
               if not gr.containsVertex(control['graph'],j['vertex']):
                  model.add_data(hash_vertex,j)
                  counter_follow_nodes+=1
                  gr.insertVertex(control['graph'],j['vertex'])
                  #model.add_data(array_vertex,j)
                  lt.addLast(array_vertex,j['vertex'])
   counter_nodes_edges =0                
   for w in lt.iterator(hash_table_per_wolf['table']):
      if w['key']!=None:
         for ver in range(0,len(w['value']['elements'])-1):
            a=w['value']['elements'][ver]['vertex']
            b=w['value']['elements'][ver+1]['vertex']
            if a!=b:
               s_list_1=a.split('_')
               s_list_2=b.split('_')
               counter_nodes_edges+=1
               gr.addEdge(control['graph'],a,b,model.haversine_equation(float(s_list_1[0].replace('m','-').replace('p','.')),float(s_list_1[1].replace('m','-').replace('p','.')),float(s_list_2[0].replace('m','-').replace('p','.')),float(s_list_2[1].replace('m','-').replace('p','.'))))
               
   for i in lt.iterator(hiper_nodes['table']):
      if i['key']!=None:
         a=list(set(i['value']['elements']))
         if len(a)>1:
            for j in a:
               model.add_data_special(hiper_nodes_list,j)
         else:
            model.add_data_special(hiper_nodes_list,a[0])

   hiper_nodes_df_lt=lt.newList(datastructure='ARRAY_LIST')
   counter_hiper_nodes=0
   counter_hiper_nodes_edges=0
   for key in lt.iterator(hiper_nodes_list['table']):
      if key['key']!=None and key['value']['size']>1:
         lt.addLast(hiper_nodes_df_lt,key['key'])
         counter_hiper_nodes+=1
         hiper_np=str(str(key['key'][0])+'_'+str(key['key'][1])).replace('.','p').replace('-','m')
         lt.addLast(five_first_last,hiper_np)
         gr.insertVertex(control['graph'],hiper_np)
         
         for k in lt.iterator(array_vertex):       
            d_split=k.split('_')
            if d_split[0]+'_'+d_split[1]==hiper_np:
               gr.addEdge(control['graph'],k,hiper_np,0)
               gr.addEdge(control['graph'],hiper_np,k,0)
               counter_hiper_nodes_edges+=2
   control['list_individuals']=list_individual_wolfs
   control['hash_table_ocurrence']=hash_table_per_wolf
   control['list_hiper_nodes']=hiper_nodes_df_lt
   control['hash_vertex']=hash_vertex
  
   return control, counter_hiper_nodes,counter_hiper_nodes_edges
   

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
   return model.req_1(load_data(control))




def req_2(control):
   """
   Retorna el resultado del requerimiento 2
   """
   # TODO: Modificar el requerimiento 2
   pass




def req_3(control):
   """
   Retorna el resultado del requerimiento 3
   """
   # TODO: Modificar el requerimiento 3
   pass




def req_4(control,lon_lat_1,lon_lat_2):
   """
   Retorna el resultado del requerimiento 4
   """
   # TODO: Modificar el requerimiento 4
   return model.req_4(control,lon_lat_1,lon_lat_2)




def req_5(control):
   """
   Retorna el resultado del requerimiento 5
   """
   # TODO: Modificar el requerimiento 5
   pass


def req_6(control,init_date,end_date,animal_sex):
   """
   Retorna el resultado del requerimiento 6
   """
   # TODO: Modificar el requerimiento 6
   return model.req_6(control,init_date,end_date,animal_sex)




def req_7(control,init_date,end_date,temp_min,temp_max):
   """
   Retorna el resultado del requerimiento 7
   """
   # TODO: Modificar el requerimiento 7
   return model.req_7(control,init_date,end_date,temp_min,temp_max)




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
