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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from datetime import datetime
from math import radians, cos, sin, asin, sqrt
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import graph as gr
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Graphs import bellmanford as bf
from DISClib.Algorithms.Graphs import bfs
from DISClib.Algorithms.Graphs import dfs
from DISClib.Algorithms.Graphs import prim
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos
'''
"ADJ_LIST"
"ADJ_MTX": ".adjlist"
'''
def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    return {'graph':gr.newGraph(datastructure="ADJ_LIST",directed=True),'list_individuals':None,'hash_table_ocurrence':None}


# Funciones para agregar informacion al modelo

def add_data(hash_table_per_wolf,data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista

    if mp.contains(hash_table_per_wolf,data['individual-id']):
        lt.addLast(mp.get(hash_table_per_wolf,data['individual-id'])['value'],data)
    else:
        value=lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(value,data)
        mp.put(hash_table_per_wolf,data['individual-id'],value)
    return hash_table_per_wolf

def add_data_hiper_nodes(hash_table_per_wolf,data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista

    if mp.contains(hash_table_per_wolf,data['individual-id']):
        lt.addLast(mp.get(hash_table_per_wolf,data['individual-id'])['value'],data['lon_lat'])
    else:
        value=lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(value,data['lon_lat'])
        mp.put(hash_table_per_wolf,data['individual-id'],value)
    return hash_table_per_wolf

def add_data_special(hash_table_per_wolf,data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista

    if mp.contains(hash_table_per_wolf,data):
        mp.get(hash_table_per_wolf,data)['value']['size']+=1
    else:
        value=lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(value,0)
        mp.put(hash_table_per_wolf,data,value)
    return hash_table_per_wolf

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    hola= bfs.BreadhtFisrtSearch(data_structs,"m111p862_57p449")
  
    return bfs.hasPathTo(hola,"m111p908_57p427")
    #return djk.pathTo(data_structs,'m111p439_56p912_13792_13792')

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs,lon_lat_1,lon_lat_2):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4

    lon_lat_1_list=lt.newList(datastructure='ARRAY_LIST')
    lon_lat_2_list=lt.newList(datastructure='ARRAY_LIST')

    for i in lt.iterator(data_structs['list_hiper_nodes']):
        lt.addLast(lon_lat_1_list,(i,haversine_equation(i[0],i[1],lon_lat_1[0],lon_lat_1[1])))
        lt.addLast(lon_lat_2_list,(i,haversine_equation(i[0],i[1],lon_lat_2[0],lon_lat_2[1])))

    lon_lat_1_nearest=lt.firstElement(quk.sort(lon_lat_1_list,cmp_harvesine))
    lon_lat_2_nearest=lt.firstElement(quk.sort(lon_lat_2_list,cmp_harvesine))
    
    lon_lat_1_nearest_converted=str(str(lon_lat_1_nearest[0][0])+'_'+str(lon_lat_1_nearest[0][1])).replace('.','p').replace('-','m')
    lon_lat_2_nearest_converted=str(str(lon_lat_2_nearest[0][0])+'_'+str(lon_lat_2_nearest[0][1])).replace('.','p').replace('-','m')
  
    graph_search=djk.Dijkstra(data_structs['graph'],lon_lat_1_nearest_converted)
    total_weight=djk.distTo(graph_search,lon_lat_2_nearest_converted)
    list_vertices_path=lt.newList(datastructure='ARRAY_LIST')
    
    for j in lt.iterator(djk.pathTo(graph_search,lon_lat_2_nearest_converted)):
        lt.addLast(list_vertices_path,j)

    hiper_nodes_route=lt.newList(datastructure='ARRAY_LIST')
    number_nodes_individuals=lt.newList(datastructure='ARRAY_LIST')
    for k in lt.iterator(list_vertices_path):
        if k['weight']==0 and len(k['vertexA'].split('_'))==2:
                lt.addLast(hiper_nodes_route,k['vertexA'])
        else:
            vertex_A=k['vertexA'].split('_')
            lt.addLast(number_nodes_individuals,vertex_A[2]+'_'+vertex_A[3])

        if k['weight']==0 and len(k['vertexB'].split('_'))==2:
                lt.addLast(hiper_nodes_route,k['vertexB'])      
        else:
            vertex_B=k['vertexB'].split('_')
            lt.addLast(number_nodes_individuals,vertex_B[2]+'_'+vertex_B[3])

    hiper_nodes_route=list(set(hiper_nodes_route['elements']))
    number_nodes_individuals=len(set(number_nodes_individuals['elements']))
    total_segments=(list_vertices_path['size']*2)-1
    
    list_3_first_last=lt.newList(datastructure='ARRAY_LIST')

    for i in set(hiper_nodes_route[:3]+hiper_nodes_route[-3:]):
        row=lt.newList(datastructure='ARRAY_LIST')
        list_adjacents_size=gr.adjacents(data_structs['graph'],i)
        adjacents_array=lt.newList(datastructure='ARRAY_LIST')
        coordinates=i.split('_')
        lon=float(coordinates[0].replace('m','-').replace('p','.'))
        lati=float(coordinates[1].replace('m','-').replace('p','.'))

        for j in lt.iterator(list_adjacents_size):
            lt.addLast(adjacents_array,j)

        lt.addLast(row,i)
        lt.addLast(row,lon)
        lt.addLast(row,lati)
        lt.addLast(row,list_adjacents_size['size'])
        lt.addLast(row,adjacents_array['elements'])

        list_hiper_node_nearest=lt.newList(datastructure='ARRAY_LIST')
        for o in lt.iterator(data_structs['list_hiper_nodes']):
            lt.addLast(list_hiper_node_nearest,(o,haversine_equation(o[0],o[1],lon,lati)))

        list_hiper_node_nearest=quk.sort(list_hiper_node_nearest,cmp_harvesine)['elements'][1]
        lt.addLast(row,str(str(list_hiper_node_nearest[0][0])+'_'+str(list_hiper_node_nearest[0][1])).replace('.','p').replace('-','m'))
        lt.addLast(list_3_first_last,row)
    
    return lon_lat_1_nearest[1], lon_lat_2_nearest[1], total_weight, len(hiper_nodes_route), number_nodes_individuals,total_segments,list_3_first_last
            
def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs,init_date,end_date,animal_sex):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    
    #Primera parte
    if animal_sex=='hembras':
        animal_sex='f'
    if animal_sex=='machos':
        animal_sex='m'

    list_indi_short=lt.newList(datastructure='ARRAY_LIST')
    list_vertex_m_f=lt.newList(datastructure='ARRAY_LIST')
    hash_filter_vertex=mp.newMap(numelements=45,loadfactor=0.75,maptype='PROBING')
    list_shortest_path=lt.newList(datastructure='ARRAY_LIST')

    for g in range(0,data_structs['list_individuals']['size']):
        if data_structs['list_individuals']['elements'][g]['animal-sex']==animal_sex:
            lt.addLast(list_indi_short,data_structs['list_individuals']['elements'][g])
            lt.addLast(list_vertex_m_f,data_structs['list_individuals']['elements'][g]['individual-id'])


    for i in lt.iterator(data_structs['hash_vertex']['table']):
        if i['key']!=None and i['key']in list_vertex_m_f['elements']:
            
            for j in lt.iterator(i['value']):
                if datetime.strptime(init_date,'%Y-%m-%d %H:%M')<=j['time_datetime']<=datetime.strptime(end_date,'%Y-%m-%d %H:%M'):
                    add_data(hash_filter_vertex,j)

    for y in lt.iterator(hash_filter_vertex['table']):
        if y['key']!=None:
            mini_graph=djk.Dijkstra(data_structs['graph'],y['value']['elements'][0]['vertex'])
            djk.pathTo(mini_graph,y['value']['elements'][-1]['vertex'])
            lt.addLast(list_shortest_path,(y['value']['elements'][-1]['individual-id'],djk.distTo(mini_graph,y['value']['elements'][-1]['vertex'])))
    
    shortest_larger_path=quk.sort(list_shortest_path,cmp_harvesine)
    shortest_path=lt.firstElement(shortest_larger_path)#0: KEY 1:DISTANCIA RECORRDIA
    larger_path=shortest_larger_path['elements'][-1]

    total_distance_shortest=mp.get(data_structs['hash_table_ocurrence'],shortest_path[0])
    total_distance_larger=mp.get(data_structs['hash_table_ocurrence'],larger_path[0])

    graph_djk_total_shortest=djk.Dijkstra(data_structs['graph'],total_distance_shortest['value']['elements'][0]['vertex'])
    path_total_shortest=djk.distTo(graph_djk_total_shortest,total_distance_shortest['value']['elements'][-1]['vertex'])#Camino

    graph_djk_total_larger=djk.Dijkstra(data_structs['graph'],total_distance_larger['value']['elements'][0]['vertex'])
    path_total_larger=djk.distTo(graph_djk_total_larger,total_distance_larger['value']['elements'][-1]['vertex'])#Camino

    s_1=mp.get(hash_filter_vertex,shortest_path[0])
    graph_djk_shortest=djk.Dijkstra(data_structs['graph'],s_1['value']['elements'][0]['vertex'])
    path_shortest=djk.pathTo(graph_djk_shortest,s_1['value']['elements'][-1]['vertex'])#Camino

    s_2=mp.get(hash_filter_vertex,larger_path[0])
    graph_djk_larger=djk.Dijkstra(data_structs['graph'],s_2['value']['elements'][0]['vertex'])
    path_larger=djk.pathTo(graph_djk_larger,s_2['value']['elements'][-1]['vertex'])#Camino
    
    list_individual_short_char=lt.newList(datastructure='ARRAY_LIST')
    list_individual_large_char=lt.newList(datastructure='ARRAY_LIST')

    for w in lt.iterator(list_indi_short):
        if w['individual-id']==shortest_path[0]:
            lt.addLast(list_individual_short_char,w)#carecteristicas
        if w['individual-id']==larger_path[0]:
            lt.addLast(list_individual_large_char,w)#carecteristicas

    hiper_nodes_route_shortest=lt.newList(datastructure='ARRAY_LIST')
    hiper_nodes_route_larger=lt.newList(datastructure='ARRAY_LIST')

    for b in lt.iterator(path_shortest):
        if b['weight']==0 and len(b['vertexA'].split('_'))==2:
                lt.addLast(hiper_nodes_route_shortest,b['vertexA'])
    
        if b['weight']==0 and len(b['vertexB'].split('_'))==2:
                lt.addLast(hiper_nodes_route_shortest,b['vertexB'])     

    for r in lt.iterator(path_larger):
        if r['weight']==0 and len(r['vertexA'].split('_'))==2:
                lt.addLast(hiper_nodes_route_larger,r['vertexA'])
    
        if r['weight']==0 and len(r['vertexB'].split('_'))==2:
                lt.addLast(hiper_nodes_route_larger,r['vertexB'])    
    
    hiper_nodes_route_shortest=list(set(hiper_nodes_route_shortest['elements']))#Lenght total hiper_nodos
    hiper_nodes_route_larger=list(set(hiper_nodes_route_larger['elements']))#Lenght total hiper_nodos

    path_larger_size=(path_larger['size']*2)-1
    path_shortest_size=(path_shortest['size']*2)-1

    list_3_first_last_shortest=lt.newList(datastructure='ARRAY_LIST')
    list_3_first_last_larger=lt.newList(datastructure='ARRAY_LIST')

    list_3_first_last_shortest=first_3_last_3(data_structs,hiper_nodes_route_shortest)    
    list_3_first_last_larger=first_3_last_3(data_structs,hiper_nodes_route_larger)
    
    list_individual_short_char['elements'][0]['total_distance']=path_total_shortest
    list_individual_large_char['elements'][0]['total_distance']=path_total_larger
    
    return list_individual_short_char['elements'][0],shortest_path[1],len(hiper_nodes_route_shortest),path_shortest_size,list_3_first_last_shortest,list_individual_large_char['elements'][0],larger_path[1],len(hiper_nodes_route_shortest),path_larger_size,list_3_first_last_larger
    
    
def req_7(data_structs,init_date,end_date,temp_min,temp_max):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento

def first_3_last_3(data_structs,lista):
    list_=lt.newList(datastructure='ARRAY_LIST')
    for p in set(lista[:3]+lista[-3:]):
        row=lt.newList(datastructure='ARRAY_LIST')
        list_adjacents_size=gr.adjacents(data_structs['graph'],p)
        adjacents_array=lt.newList(datastructure='ARRAY_LIST')
        coordinates=p.split('_')
        lon=float(coordinates[0].replace('m','-').replace('p','.'))
        lati=float(coordinates[1].replace('m','-').replace('p','.'))

        for j in lt.iterator(list_adjacents_size):
            lt.addLast(adjacents_array,j)

        lt.addLast(row,p)
        lt.addLast(row,lon)
        lt.addLast(row,lati)
        lt.addLast(row,list_adjacents_size['size'])
        lt.addLast(row,adjacents_array['elements'])
        lt.addLast(list_,row['elements'])
    return list_['elements']
def cmp_harvesine(data_1,data_2):
    return data_1[1]<=data_2[1]

def cmp_time(data_1,data_2):
    return data_1['time_datetime']<=data_2['time_datetime']
def haversine_equation(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = radians(float(lon1)),radians(float(lat1)),radians(float(lon2)),radians(float(lat2))
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371
    return round(c * r,3)
