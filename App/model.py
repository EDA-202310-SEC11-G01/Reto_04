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


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs,origen,destino):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    dist=0
    contador=1
    grafo=dfs.DepthFirstSearch(data_structs["graph"],origen)
    pila=dfs.pathTo(grafo,destino)
    nodo=origen
    total_seg=0
    total_enc=0
    salida=st.newStack()
    size=st.size(pila) 
    xcosa=st.pop(pila)
    st.push(salida,xcosa)
    lista_lobos=lt.newList()

    while pila is not None and not lt.isEmpty(pila):
        nodo2=st.pop(pila)
        edge=round(gr.getEdge(data_structs["graph"],nodo,nodo2)["weight"],3)
        dist+=edge
        ide=nodo
        lon=nodo[:8].replace("m","-").replace("p",".")
        lat=nodo[9:15].replace("m","-").replace("p",".")
        num_ind=gr.degree(data_structs["graph"],nodo)
        lobos_adj=gr.adjacents(data_structs["graph"],nodo)
        e=0

        for j in lt.iterator(lobos_adj):
            if e<3 or (e<= lt.size(lobos_adj) and e>=lt.size(lobos_adj)-3):
                lt.addLast(lista_lobos,j)
            e+=1


        dicci={"id":ide,"longitud":lon,"latitud":lat,"numero individuos":num_ind,"lobos":lista_lobos,"distancia al siguiente vértice":edge,"siguiente vértice":nodo2}
        if edge !=0:
            total_seg+=1
        else:
            total_enc+=1

        if contador <5 or (contador <= size and contador>=size-5):
            st.push(salida,dicci)

        nodo=nodo2
        contador+=1
    tupla=(dist,total_enc,total_seg,salida)
    return tupla
    




def req_2(data_structs,origen,destino):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    dist=0
    contador=1
    grafo=bf.BellmanFord(data_structs["graph"],origen)
    pila=bf.pathTo(grafo,destino)
    total_seg=0
    total_enc=0
    salida=st.newStack()
    size=st.size(pila) 
    lista_lobos=lt.newList()
    reves=st.newStack()
    for w in lt.iterator(pila):
        st.push(reves,w)
    for e in lt.iterator(reves):
        edge=round(e["weight"])
        dist+=edge
        ide=e["vertexA"]
        lon=e["vertexA"][:8].replace("m","-").replace("p",".")
        lat=e["vertexA"][9:15].replace("m","-").replace("p",".")
        num_ind=gr.degree(data_structs["graph"],e["vertexA"])
        lobos_adj=gr.adjacents(data_structs["graph"],e["vertexA"])
        i=0

        for j in lt.iterator(lobos_adj):
            if i<3 or (i<= lt.size(lobos_adj) and i>=lt.size(lobos_adj)-3):
                lt.addLast(lista_lobos,j)
            i+=1


        dicci={"id":ide,"longitud":lon,"latitud":lat,"numero individuos":num_ind,"lobos":lista_lobos,"distancia al siguiente vértice":edge,"siguiente vértice":e["vertexB"]}
        if edge !=0:
            total_seg+=1
        else:
            total_enc+=1

        if contador <5 or (contador <= size and contador>=size-5):
            st.push(salida,dicci)

        contador+=1
    for x in lt.iterator(salida):
        print(x)
    tupla=(dist,total_enc,total_seg,salida)
    #return tupla

def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs,origen,distancia,numero):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    distancia=distancia/2
    estructura=prim.PrimMST(data_structs["graph"],origen)
    algo=prim.scan(data_structs["graph"],estructura,origen)
    dist=0
    puntos=0
    ind=0
    mapa=mp.newMap()
    lista_ind=lt.newList()
    lista_puntos=lt.newList()
    #print(estructura)
    for a in lt.iterator(algo["keys"]): 
        lt.addLast(lista_puntos,a)
        puntos+=1
        ind=gr.degree(data_structs["graph"],a)
        lt.addLast(ind)
        for j in lt.iterator(algo["values"]):
            dist+=j["index"]


        mp.put(mapa,"número de puntos",puntos)
        mp.put(mapa,"distancia recorrida",dist)
        mp.put(mapa,"listado de puntos",lista_puntos)
        mp.put(mapa,"número de individuos",lista_ind)
        if (dist<=distancia or dist>distancia-5) and (puntos>numero):
            return mapa
        
            


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


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


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def cmp_time(data_1,data_2):
    return data_1['time_datetime']<=data_2['time_datetime']
def haversine_equation(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = radians(float(lon1)),radians(float(lat1)),radians(float(lon2)),radians(float(lat2))
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371
    return c * r
