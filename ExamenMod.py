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



def cargar_lista(nombreFichero):
   with open(nombreFichero,"r") as fichero:
    listacanciones=[]
    for linea in fichero:
        libreria = {}
        cancion,artista,genero = linea.strip().split(" - ") 
        libreria["Nombre"] = cancion
        libreria["Artista"] = artista
        libreria["Genero"] = genero
        listacanciones.append(libreria)

    return listacanciones

def buscar_cancion(canciones,nombre):
    encontrada = False
    for i in canciones:
        if i["Nombre"] == nombre:
            encontrada = True
            return encontrada
        
    return encontrada

def agregar_cancion(canciones,nombrecancion,nombreartista,nombregenero):
    if buscar_cancion(canciones,nombrecancion) == False:
        cancion = {}
        cancion["Nombre"] = nombrecancion
        cancion["Artista"] = nombreartista
        cancion["Genero"] = nombregenero
        canciones.append(cancion)
    else:
        print(f"La cancion {nombrecancion} ya existe")

#cargar lista
#agregar cancion
#eliminar cancion
#guardar lista

#FALLO GORDO, DECLARADO PRIMERO ARTISTA ANTES QUE CANCIÓN, TODO SALE DEL REVÉS
#OTRO FALLO GORDO EN EL USO DEL SPLIT, ME SALÍAN LAS CANCIONES CON SEPARACIÓN AL FINAL Y ARTISTAS CON SEPARACION AL PRINCIPIO

#agrega los valores a la lista que pasan como parametros

def eliminar_cancion(listacanciones,cancion):
    if cancion in listacanciones:
        del listacanciones[cancion] 

#USADA MAL LA SENTENCIA DEL, FALLO GORDO 

def guardar_lista(listacanciones, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo: #usamos w para ecribir
        for cancion, artista in listacanciones.items(): #for para recorrer los items
            linea = f"{cancion} - {artista}\n" #maquetacion de linea que sera escrita
            archivo.write(linea) #usamos .write para escribir, parará cuando no queden mas items en el diccionario


canciones = cargar_lista("playlist2.txt")
print(canciones)
agregar_cancion(canciones,"Ferxxo 100","Alvarito Diaz","Romantico")
print(canciones)

#agregar_cancion(listacanciones,"feid","ferxxo100")
#print(listacanciones)
#funciona

#eliminar_cancion(listacanciones,"ferxxo100")
#print(listacanciones)
#funciona







