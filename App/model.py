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
from datetime import datetime
assert cf
import tabulate as tb
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
    return {'graph':gr.newGraph(datastructure="ADJ_MTX",directed=True),'list_individuals':None,'hash_table_ocurrence':None}
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
def add_data_new_graph(hash_table_per_wolf,data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista

    if mp.contains(hash_table_per_wolf,str(data['value'])):
        lt.addLast(mp.get(hash_table_per_wolf,str(data['value']))['value'],data['key'])
    else:
        value=lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(value,data['key'])
        mp.put(hash_table_per_wolf,str(data['value']),value)
    return hash_table_per_wolf
def req_1(data_structs,origen,destino):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    dist=0
    contador=0
    grafo=dfs.DepthFirstSearch(data_structs["graph"],origen)
    pila=dfs.pathTo(grafo,destino)
    nodo=origen
    total_seg=0
    total_enc=0
    salida=st.newStack()
    size=st.size(pila) 
    xcosa=st.pop(pila)
    #st.push(salida,xcosa)
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
        lista_lista_lobos=lt.newList(datastructure='ARRAY_LIST')
        for i in lt.iterator(lista_lobos):
            lt.addLast(lista_lista_lobos,i)

        dicci={"id":ide,"longitud":lon,"latitud":lat,"numero individuos":num_ind,"lobos":set(lista_lista_lobos['elements'][:3]+lista_lista_lobos['elements'][-3:]),"distancia al siguiente vértice":edge,"siguiente vértice":nodo2}
        if edge !=0:
            total_seg+=1
        else:
            total_enc+=1
        if contador <5 or (contador <= size and contador>=size-6):
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

        lista_lista_lobos=lt.newList(datastructure='ARRAY_LIST')
        for k in lt.iterator(lista_lobos):
            lt.addLast(lista_lista_lobos,k)

        dicci={"id":ide,"longitud":lon,"latitud":lat,"numero individuos":num_ind,"lobos":set(lista_lista_lobos['elements'][:3]+lista_lista_lobos['elements'][-3:]),"distancia al siguiente vértice":edge,"siguiente vértice":e["vertexB"]}
        if edge !=0:
            total_seg+=1
        else:
            total_enc+=1
        if contador <5 or (contador <= size and contador>=size-5):
            st.push(salida,dicci)
        contador+=1
    tupla=(dist,total_enc,total_seg,salida)
    return tupla
def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    
    sccmap, sc = kosaraju(data_structs) #Aca ya tenemos el sccmap en el que estan los IDCC con sus respectivas componentes
    top_5_IDCC = top_5_scc(sccmap) #Y aca el top 5 de los IDCC que mas componentes tienen.
    
    llaves = mp.keySet(top_5_IDCC)
    dataframe = lt.newList("ARRAY_LIST")
    
    #Este ciclo solo se hara 5 veces, por el top 5
    for key2 in lt.iterator(llaves): #Aca vamos a recorrer la lista de codigos en los 5 casos. Para extraer la info de cada uno.
        longitudes = lt.newList("ARRAY_LIST")
        latitudes = lt.newList("ARRAY_LIST")
        wolfs_id = lt.newList("ARRAY_LIST")
        entry = mp.get(top_5_IDCC, key2)
        lista = me.getValue(entry)
        
        for node in lt.iterator(lista):
            longitude, latitude, id_animal = extract_info(node) #Extraccion de latitudes, codigos de lobo y longitudes.
            lt.addLast(latitudes, float(latitude))
            lt.addLast(longitudes, float(longitude))
            if id_animal not in wolfs_id["elements"] and id_animal != '':
                lt.addLast(wolfs_id, id_animal)        
        
        wolf_count = lt.size(wolfs_id)
        top3_nodes = lt.subList(lista, 0, 3)
        bot3_nodes = lt.subList(lista, lt.size(lista)-2, 3)
        
        #Para evitar tener que recorrer todas las listas buscando por el max y el min.
        #QUise utilizar minpq pero no encontre maxpq asi q no lo implemente.
        max_lat = max(latitudes["elements"])
        max_long = max(longitudes["elements"])
        min_lat = min(latitudes["elements"])
        min_long = min(longitudes["elements"])
    
        if wolf_count <= 5:
            top3 = wolfs_id
            bot3 = top3
        #Esto es mera cortesia por si acaso hay mas de 5 lobos en la lista. pero no pasa.
        else:
            top3 = lt.subList(wolfs_id, 0, 3)
            bot3 = lt.subList(wolfs_id, (wolf_count)-2, 3)
                                        
        lista_final = lt.newList("ARRAY_LIST")
        ids_finales = lt.newList("ARRAY_LIST")
        for wolf in lt.iterator(data_structs["list_individuals"]):
            for t3 in lt.iterator(top3):
                #Comprobamos que el del top sea el mismo que el de la lista final 
                #y si lo es le quitamos el id a la lista y lo metemos en la lista final de lobos.
                if wolf["animal-id"] in t3 and wolf["animal-id"] not in ids_finales["elements"]: #Para que no se repitan los lobos
                    lt.addLast(lista_final, wolf)
                    lt.addLast(ids_finales, wolf["animal-id"])
                
        #Esto ya es para el view
        lista_lobos = lt.newList("ARRAY_LIST")
        
        for wolf in lt.iterator(lista_final):
            w_id = wolf["animal-id"]
            w_sex = wolf["animal-sex"]
            w_life = wolf["animal-life-stage"]
            w_study = wolf["study-site"]
            w_comments = wolf["deployment-comments"]
            lt.addLast(lista_lobos, [w_id, w_sex, w_life, w_study, w_comments])
            
        lista_lobos_def = lista_lobos_fix(lista_lobos)
        headers=["individual-id", "animal-sex", "animal-life-stage", "study-site", "deployment-comments"]
        #Empaquetamos la lista ya tabulada para no tener que hacer mas ciclos en el view.
        lista_lobos_tabulada = tb.tabulate(lista_lobos_def["elements"], headers=headers, maxheadercolwidths= [12, 12, 12, 12, 15], maxcolwidths= [12, 12, 12, 12, 15], tablefmt="fancy_grid")
        #Sacamos las demas variables que necesitamos para el view.
        nodes = get_nodes(top3_nodes, bot3_nodes) 
        entry_idsc = mp.get(sc["idscc"], lt.firstElement(top3_nodes))
        idscc = me.getValue(entry_idsc)
        lt.addLast(dataframe, [idscc, nodes, key2, min_lat, max_lat, \
            min_long, max_long, wolf_count, lista_lobos_tabulada])
    return dataframe

def kosaraju(data_structs):
    
    """Genera el mapa de componentes fuertemente conectadas
    utilizando el algoritmo de kosaraju."""
    
    sc = scc.KosarajuSCC(data_structs["graph"])
    scmarked = sc["marked"]
    marks = lt.newList("ARRAY_LIST")
    componentes = sc["idscc"]
    sccmap = mp.newMap(maptype="PROBING")
    for key in lt.iterator(mp.keySet(componentes)):
        entry = mp.get(componentes, key)
        valor = me.getValue(entry)
        if lt.isPresent(marks, valor) == 0:
            lt.addLast(marks, valor)
            comp_list = lt.newList("ARRAY_LIST")
            lt.addLast(comp_list, key)
            mp.put(sccmap, valor, comp_list)
        else: 
            entry1 = mp.get(sccmap, valor)
            value1 = me.getValue(entry1)
            lt.addLast(value1, key)
            
    return sccmap, sc
def top_5_scc(sccmap):
    
    """Genera el top 5 de las componentes fuertemente conectadas.
    Recorriendo el mapa de componentes fuertemente conectadas y extrayendo las que
    mas tienen nodos adentro."""
    
    lista_cc = lt.newList("ARRAY_LIST")
    size_list = lt.newList("ARRAY_LIST")
    scc_val = mp.newMap(maptype="PROBING")
    top_5_scc = mp.newMap(maptype="PROBING")
    for key1 in lt.iterator(mp.keySet(sccmap)):
        lt.addLast(lista_cc, key1)
        entry = mp.get(sccmap, key1)
        lst = me.getValue(entry)
        size = lt.size(lst)
        lt.addLast(size_list, size)
        mp.put(scc_val, size, lst)
    size_list = sorted(size_list["elements"], reverse=True)
    for i in range(0, 5):
        mp.put(top_5_scc, size_list[i], me.getValue(mp.get(scc_val, size_list[i])))
    return top_5_scc

def extract_info(code):
    
    """Esta funcion va a extraer la informacion de los codigos de los lobos
    que estan en este formato: m111p439_56p912_1372_1379 o m111p496_57p353"""
    
    longitud = ''
    latitud = ''
    wolf_id = ''
    first_m = False
    first_p = False
    is_latitud = False
    is_wolf = False
    first_p_lat = False
    skip_first_underscore = False
    for letra in code:
        if not first_m or not first_p:
            if letra == 'm':
                longitud += '-'
                first_m = True
            elif letra == 'p':
                longitud += '.'
                first_p = True
            elif letra != 'p' and letra != 'm':
                longitud += letra
        #Aca comprobamos si ya se cumplio el primer if osea 
        #Ya se recorrio el m111p pero luego siguen los 3 digitos despues del .
        elif first_m and first_p and not is_latitud:
            if letra == '_':
                is_latitud = True
            else: 
                longitud += letra
        #Aca ya estamos en la siguiente iteracion que seria cuando 
        #Va despues del _ osea 57p474
        elif is_latitud and letra != '_' and not is_wolf:
            if not first_p_lat:
                if letra == 'p':
                    latitud += '.'
                    first_p_lat = True
                else: 
                    latitud += letra
            else: 
                latitud += letra
        elif first_p_lat and not is_wolf:
            if letra == '_':
                is_wolf = True
            else: 
                latitud += letra
        if is_wolf and letra != '_' and skip_first_underscore == False:
            wolf_id += letra
            skip_first_underscore = True
        if is_wolf and skip_first_underscore:
            wolf_id += letra
    return longitud, latitud, wolf_id
    
def get_nodes(top3, bot3):
    
    """Recibe los top 3 y bot 3 de los nodos 
    y devuelve el formato deseado para el view"""
    
    final_string = ''
    first = True
    for node in lt.iterator(top3):
        if first:
          final_string += node
        else:
            final_string += ', ' + node
        first = False
    final_string += ','
    final_string += '...,'
    firstt = True
    for nodo in lt.iterator(bot3):
        if firstt:
          final_string += nodo
        else:
            final_string += ', ' + nodo
        firstt = False
        
    return final_string
    
def lista_lobos_fix(lista_lobos):
    
    """Recibe una lista de lobos y con esa lista cambia
    Los '' por unknown."""
    
    for element in lt.iterator(lista_lobos):
        for i in range(len(element)):#Aca tenemos el individual-id, animal sex etc. 
            if element[i] == '':#Osea se chequea por cada atributo que tenga el lobo
                element[i] = 'Unknown'
    return lista_lobos
    
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
        vertex_A=k['vertexA'].split('_')
        vertex_B=k['vertexB'].split('_')
        if k['weight']==0 and len(vertex_A)==2:
                lt.addLast(hiper_nodes_route,k['vertexA'])
        else:
            if len(vertex_A)==6:
                lt.addLast(number_nodes_individuals,vertex_A[2]+'_'+vertex_A[3]+'_'+vertex_A[4]+'_'+vertex_A[5])
            elif len(vertex_A)==5:
                lt.addLast(number_nodes_individuals,vertex_A[2]+'_'+vertex_A[3]+'_'+vertex_A[4])
            else:
                lt.addLast(number_nodes_individuals,vertex_A[2]+'_'+vertex_A[3])    
        if k['weight']==0 and len(vertex_B)==2:
                lt.addLast(hiper_nodes_route,k['vertexB'])      
        else:
            if len(vertex_B)==6:
                lt.addLast(number_nodes_individuals,vertex_B[2]+'_'+vertex_B[3]+'_'+vertex_B[4]+'_'+vertex_B[5])
            elif len(vertex_B)==5:
                lt.addLast(number_nodes_individuals,vertex_B[2]+'_'+vertex_B[3]+'_'+vertex_B[4])
            else:
                lt.addLast(number_nodes_individuals,vertex_B[2]+'_'+vertex_B[3])    
           
    hiper_nodes_route=list(set(hiper_nodes_route['elements']))
    number_nodes_individuals=len(set(number_nodes_individuals['elements']))
    total_segments=(list_vertices_path['size'])-1
    
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
        lt.addLast(row,adjacents_array['size'])
        lt.addLast(row,set(adjacents_array['elements'][:3]+adjacents_array['elements'][-3:]))
        
        list_hiper_node_nearest=lt.newList(datastructure='ARRAY_LIST')
        for o in lt.iterator(data_structs['list_hiper_nodes']):
            lt.addLast(list_hiper_node_nearest,(o,haversine_equation(o[0],o[1],lon,lati)))
        list_hiper_node_nearest=quk.sort(list_hiper_node_nearest,cmp_harvesine)['elements'][1]
        lt.addLast(row,list_hiper_node_nearest[1])
        lt.addLast(list_3_first_last,row['elements'])
    
    return lon_lat_1_nearest[1], lon_lat_2_nearest[1], total_weight, len(hiper_nodes_route), number_nodes_individuals,total_segments,list_3_first_last['elements']
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

    path_larger_size=(path_larger['size'])-1
    path_shortest_size=(path_shortest['size'])-1

    list_3_first_last_shortest=lt.newList(datastructure='ARRAY_LIST')
    list_3_first_last_larger=lt.newList(datastructure='ARRAY_LIST')

    list_3_first_last_shortest=first_3_last_3(data_structs,hiper_nodes_route_shortest)    
    list_3_first_last_larger=first_3_last_3(data_structs,hiper_nodes_route_larger)
    
    list_individual_short_char['elements'][0]['total_distance']=path_total_shortest
    list_individual_large_char['elements'][0]['total_distance']=path_total_larger
    
    return list_individual_short_char['elements'][0],shortest_path[1],len(hiper_nodes_route_shortest),path_shortest_size,list_3_first_last_shortest,list_individual_large_char['elements'][0],larger_path[1],len(hiper_nodes_route_larger),path_larger_size,list_3_first_last_larger
    
def req_7(data_structs,init_date,end_date,temp_min,temp_max):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7

    new_graph=gr.newGraph(datastructure="ADJ_MTX",directed=True)
    init_date=datetime.strptime(init_date,'%Y-%m-%d %H:%M')
    end_date=datetime.strptime(end_date,'%Y-%m-%d %H:%M')
    list_individual_id_selected=lt.newList(datastructure='ARRAY_LIST')
    hash_table_filtered=mp.newMap(numelements=45,loadfactor=0.75,maptype='PROBING')
    hiper_nodes=mp.newMap(numelements=45,loadfactor=0.75,maptype='PROBING')
    hiper_nodes_list=mp.newMap(numelements=45,loadfactor=0.75,maptype='PROBING')
    array_vertex=lt.newList(datastructure='ARRAY_LIST')
    components=mp.newMap(numelements=45,loadfactor=0.75,maptype='PROBING')
    list_components=lt.newList(datastructure='ARRAY_LIST')

    for i in lt.iterator(data_structs['list_individuals']):
        if len(i['deploy-on-date'])!=0:
            if datetime.strptime(i['deploy-on-date'],'%Y-%m-%d %H:%M')>=init_date:
                if len(i['deploy-off-date'])==0 or datetime.strptime(i['deploy-off-date'],'%Y-%m-%d %H:%M')<=end_date:
                    lt.addLast(list_individual_id_selected,i['individual-id'])
        else:
            lt.addLast(list_individual_id_selected,i['individual-id'])
    
    for j in lt.iterator(data_structs['hash_table_ocurrence']['table']):
        if j['key']!=None and j['key'] in list_individual_id_selected['elements']:
            for k in lt.iterator(j['value']):
                if temp_min<=float(k['external-temperature'])<=temp_max and init_date<=k['time_datetime']<=end_date:
                    add_data(hash_table_filtered,k)
                    add_data_hiper_nodes(hiper_nodes,k)
                    if not gr.containsVertex(new_graph,k['vertex']):
                        gr.insertVertex(new_graph,k['vertex'])
                        lt.addLast(array_vertex,k['vertex'])
    for w in lt.iterator(hash_table_filtered['table']):
        if w['key']!=None:
            for ver in range(0,len(w['value']['elements'])-1):
                a=w['value']['elements'][ver]['vertex']
                b=w['value']['elements'][ver+1]['vertex']
                if a!=b:
                    s_list_1=a.split('_')
                    s_list_2=b.split('_')
                    gr.addEdge(new_graph,a,b,haversine_equation(float(s_list_1[0].replace('m','-').replace('p','.')),float(s_list_1[1].replace('m','-').replace('p','.')),float(s_list_2[0].replace('m','-').replace('p','.')),float(s_list_2[1].replace('m','-').replace('p','.'))))

    for r in lt.iterator(hiper_nodes['table']):
        if r['key']!=None:
            a=list(set(r['value']['elements']))
            if len(a)>1:
                for u in a:
                    add_data_special(hiper_nodes_list,u)
            else:
                add_data_special(hiper_nodes_list,a[0])

    for key in lt.iterator(hiper_nodes_list['table']):
        if key['key']!=None and key['value']['size']>1:
            hiper_np=str(str(key['key'][0])+'_'+str(key['key'][1])).replace('.','p').replace('-','m')
            gr.insertVertex(new_graph,hiper_np)
            for k in lt.iterator(array_vertex):
                d_split=k.split('_')
                if d_split[0]+'_'+d_split[1]==hiper_np:
                    gr.addEdge(new_graph,k,hiper_np,0)
                    gr.addEdge(new_graph,hiper_np,k,0)
    
    scc_graph=scc.KosarajuSCC(new_graph)
    for h in lt.iterator(scc_graph['idscc']['table']):
        if h['key']!=None:
            add_data_new_graph(components,h)

    for i in lt.iterator(components['table']):
        if i['key']!=None:
            lt.addLast(list_components,i)

    list_territories=quk.sort(list_components,cmp_hash_table)#numero de mandas
    
    list_territories_first_last=list_territories['elements'][:3]+list_territories['elements'][-3:]

    rows=lt.newList(datastructure='ARRAY_LIST')

    for x in list_territories_first_last:        
        hiper_nodes_sub_list=lt.newList(datastructure='ARRAY_LIST')#SIZE_HIPERNODOS
        herd_members=lt.newList(datastructure='ARRAY_LIST')#size_miembros manada

        tua=nua(x['value'])
        hiper_nodes_sub_list=tua[0]
        herd_members=tua[1]

        hiper_nodes_sub_list_3_first_last=set(hiper_nodes_sub_list['elements'][:3]+hiper_nodes_sub_list['elements'][-3:])#lista_nodos_3_first_last

        herd_members_3_first_last=set(herd_members['elements'][:3]+herd_members['elements'][-3:])#lista_members_3_first_last

        list_wolf_details=lt.newList(datastructure='ARRAY_LIST')#Detalles del lobo

        for f in herd_members_3_first_last:
            for s in lt.iterator(data_structs['list_individuals']):
                if s['individual-id']==f:
                    lt.addLast(list_wolf_details,s)
        
        list_lon=lt.newList(datastructure='ARRAY_LIST')
        list_lat=lt.newList(datastructure='ARRAY_LIST')
        if len(hiper_nodes_sub_list_3_first_last)==0:
            lt.addLast(list_lon,'None')
            lt.addLast(list_lat,'None')

        for ab in hiper_nodes_sub_list_3_first_last:
            ab_list=ab.split('_')
            lt.addLast(list_lon,float(ab_list[0].replace('m','-').replace('p','.')))
            lt.addLast(list_lat,float(ab_list[1].replace('m','-').replace('p','.')))

        me_ma_lat=quk.sort(list_lon,cmp_lon_lat)['elements']#menor:0 mayor:-1  LON
        me_ma_lon=quk.sort(list_lat,cmp_lon_lat)['elements']#menor:0 mayor:-1 LAT
        lt.addLast(rows,[hiper_nodes_sub_list['size'],hiper_nodes_sub_list_3_first_last,herd_members['size'],list_wolf_details['elements'],me_ma_lat[0],me_ma_lat[-1],me_ma_lon[0],me_ma_lon[-1]])

    largest_territorie=lt.newList(datastructure='ARRAY_LIST')
    for cd in lt.iterator(list_territories):
        semi_djk_graph=djk.Dijkstra(new_graph,cd['value']['elements'][0])
        lt.addLast(largest_territorie,(cd['key'],djk.distTo(semi_djk_graph,cd['value']['elements'][-1])))

    largest_path_territorie=quk.sort(largest_territorie,cmp_harvesine)['elements'][-1]
    part_2=lt.newList(datastructure='ARRAY_LIST')

    for fr in lt.iterator(list_territories):
        
        #distancia larga recorrida
        if largest_path_territorie[0]==fr['key']:

            
            semi_djk_graph=djk.Dijkstra(new_graph,fr['value']['elements'][0])
            path_largest=djk.pathTo(semi_djk_graph,fr['value']['elements'][-1])

            # numero de puentes
            fua=nua(fr['value'])
            list_hiper_nodes=fua[0]#Contador hiper_nodos
            list_individuals=fua[1]#contador individuos


            first_last_3_hiper_nodes=set([fr['value']['elements'][0]]+list_hiper_nodes['elements'][:3]+list_hiper_nodes['elements'][-3:]+[fr['value']['elements'][-1]])
            first_last_3_individuals=set(list_individuals['elements'][:3]+list_individuals['elements'][-3:])
            
            lt.addLast(part_2,[largest_path_territorie[1],list_hiper_nodes['size'],(path_largest['size'])-1,first_last_3_hiper_nodes,set(list_individuals['elements']),first_last_3_individuals])
    return scc.connectedComponents(scc_graph),rows['elements'],part_2['elements']
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
def cmp_Num(n1, n2):
    """
    Compara dos numeors
    """
    n1, n2 = int(n1), int(n2)
    if (n1 == n2):
        return 0
    elif (n1 > n2):
        return -1
    else:
        return 1
    
def cmpIDSSS(dato1,dato2):
    dato1 = dato1.split('-')
    dato2 = dato2.split('-')
    if  ('T' in dato1[0])and ('T' in dato2[0]):
       
        if (int(dato1[1]) > int(dato2[1])):
            
            return -1
        
        elif (int(dato1[1]) < int(dato2[1])):
            
            return 1
        
    elif ('T' in dato1[0]):
        
        return 1
    
    elif ('T' in dato2[0]):
        
        return -1
    
    elif (int(dato1[0]) == int(dato2[0])):
        
        if (dato1[1] > dato2[1]):
            
            return -1
        
        elif (dato1[1] < dato2[1]):
            
            return 1
        else:
            return 0
        
    elif (int(dato1[0]) > int(dato2[0])):
        return -1
    
    elif (int(dato1[0]) < int(dato2[0])):
        return 1
    
def cmp_time(data_1,data_2):
    return data_1['time_datetime']<=data_2['time_datetime']
def haversine_equation(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = radians(float(lon1)),radians(float(lat1)),radians(float(lon2)),radians(float(lat2))
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371
    return round((c * r),3)
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

def cmp_hash_table(data_1,data_2):
    return data_1['value']['size']>=data_2['value']['size']

def cmp_lon_lat(data_1,data_2):
    return data_1<=data_2

def cmp_harvesine(data_1,data_2):
    return data_1[1]<=data_2[1]
def nua(lista):
    hiper_nodes_sub_list=lt.newList(datastructure='ARRAY_LIST')
    herd_members=lt.newList(datastructure='ARRAY_LIST')
    for q in lt.iterator(lista):
        qua=q.split('_')

        if len(qua)==2:
            lt.addLast(hiper_nodes_sub_list,q)
        if len(qua)>2:
            if len(qua)==6:
                lt.addLast(herd_members,qua[2]+'_'+qua[3]+'_'+qua[4]+'_'+qua[5])
            elif len(qua)==5:
                lt.addLast(herd_members,qua[2]+'_'+qua[3]+'_'+qua[4])
            else:
                lt.addLast(herd_members,qua[2]+'_'+qua[3])    
    return hiper_nodes_sub_list,herd_members

