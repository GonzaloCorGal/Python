import random
import json

def cargar_lista(nombreFichero):
   with open(nombreFichero,"r") as fichero:
    listacanciones=[]
    try:
        for linea in fichero:
            libreria = {}
            cancion,artista,genero = linea.strip().split(" - ") 
            libreria["Nombre"] = cancion
            libreria["Artista"] = artista
            libreria["Genero"] = genero
            listacanciones.append(libreria)

        return listacanciones
    except(FileNotFoundError):
        print("Archivo no encontrado")
        

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

def eliminar_cancion(listacanciones,nombrecancion):
    if buscar_cancion(canciones,nombrecancion) == True:
        for i in canciones:
            if i.get("Nombre") == nombrecancion:
              canciones.remove(i)  
    else:
        print(f"La cancion {nombrecancion} no existe")

def guardar_lista(listacanciones, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo: #usamos w para ecribir
        for cancion, artista in listacanciones.items(): #for para recorrer los items
            linea = f"{cancion} - {artista}\n" #maquetacion de linea que sera escrita
            archivo.write(linea) #usamos .write para escribir, parará cuando no queden mas items en el diccionario

#def cargar_json(nombreFichero):

    


def guardar_json(canciones,nombre_Archivo):
    with open(nombre_Archivo,"w") as fichero:
      json.dump(canciones,fichero)  


canciones = cargar_lista("playlist2.txt")
print(canciones)

agregar_cancion(canciones,"XQ ERES ASI","Alvarito Diaz","Romantico")
print(canciones)

eliminar_cancion(canciones,"Tu cuerpo me llama")
print(canciones)
#funciona

guardar_json(canciones,"jsonFichero")






