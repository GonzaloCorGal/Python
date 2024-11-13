#linea.strip().split(“-”)
#fichero.close
#fichero.write(cosas)

#del
#len()
#strip
#split()

#Escribe una función llamada cargar_lista que tome el nombre de un 
#archivo de texto como argumento y devuelva un diccionario de canciones. 
#Cada clave del diccionario debe ser el título de una canción y cada valor debe ser 
#el nombre del artista.

import random

listacanciones={}

def cargar_lista():
    fichero = open("playlist.txt","r")
    for linea in fichero:
        cancion,artista = linea.strip().split(" - ") 
        listacanciones[cancion] = artista
    fichero.close()

#FALLO GORDO, DECLARADO PRIMERO ARTISTA ANTES QUE CANCIÓN, TODO SALE DEL REVÉS
#OTRO FALLO GORDO EN EL USO DEL SPLIT, ME SALÍAN LAS CANCIONES CON SEPARACIÓN AL FINAL Y ARTISTAS CON SEPARACION AL PRINCIPIO

def agregar_cancion(listacanciones,artista,cancion):
    listacanciones[cancion] = artista

#agrega los valores a la lista que pasan como parametros

def eliminar_cancion(listacanciones,cancion):
    if cancion in listacanciones:
        del listacanciones[cancion] 

#USADA MAL LA SENTENCIA DEL, FALLO GORDO 

def contar_canciones(listacanciones):
    total= len(listacanciones)
    return print(total)

#FALLO GORDO, MAL USO DEL LEN, NO ERA LISTACANCIONES.LEN ESTO NO ES JAVA
#MAL USO DEL RETURN, DEVUELVE ALGO QUE VALGA O QUE SE PUEDA USAR


def buscar_por_artista(listacanciones,artista):
    canciones_del_artista = [cancion for cancion, artista_nombre in listacanciones.items() if artista_nombre == artista]
    
    if canciones_del_artista:
        print(f"Las canciones de '{artista}' son: {', '.join(canciones_del_artista)}")
    else:
        print(f"No se encontraron canciones de '{artista}' en el diccionario.")
    
    return canciones_del_artista

#mal uso del return de nuevo, da algo que sirva de vuelta
#AFECTABA EL MAL USO DEL SPLIT, JAMAS PILLABA ARTISTAS PORQUE SIEMPRE HABÍA UNA SEPARACIÓN AL PRINCIPIO

def ordenar_alfabeticamente(listacanciones):
    listado = (sorted(listacanciones.items()))
    return print(listado)
    
#fallo de no usar el return de bien
#he usado .get cosa que hace que casque, hace falta el .items, que devuelve todos los valores del diccionario

def crear_lista_aleatoria(listacanciones,num):
    canciones_lista = list(listacanciones.items()) #lista auxiliar que mete todo el contenido de el diccionario
    num = min(num, len(canciones_lista)) #usamos la funcion min, que es una funcion que devuleve el menor de los valores a o b, en este caso tenemos
    #así aunque el usuario de un numero mayor a las canciones siempre estará limitado, y se ajustará a lo pedido por el usuario
    seleccionadas = []
    while len(seleccionadas) < num:
        cancion_aleatoria = random.choice(canciones_lista)
        if cancion_aleatoria not in seleccionadas:
            seleccionadas.append(cancion_aleatoria)
    
    return print(seleccionadas)

def guardar_lista(listacanciones, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo: #usamos w para ecribir
        for cancion, artista in listacanciones.items(): #for para recorrer los items
            linea = f"{cancion} - {artista}\n" #maquetacion de linea que sera escrita
            archivo.write(linea) #usamos .write para escribir, parará cuando no queden mas items en el diccionario


cargar_lista()
#print(listacanciones)
#funciona

#agregar_cancion(listacanciones,"feid","ferxxo100")
#print(listacanciones)
#funciona

#eliminar_cancion(listacanciones,"ferxxo100")
#print(listacanciones)
#funciona

#contar_canciones(listacanciones)
#funciona

#buscar_por_artista(listacanciones,"Bob Dylan")
#funciona

#ordenar_alfabeticamente(listacanciones)
#funciona

#crear_lista_aleatoria(listacanciones,7)
#funciona

guardar_lista(listacanciones,"ListaDescarga")




