import json

def cargar_datos(fichero):
    with open(fichero, 'r', encoding='utf-8') as contenido:
        datos = json.load(contenido)
    return datos

def guardar_datos(nombreArchivo, contenido):
    with open(nombreArchivo, 'w', encoding='utf-8') as archivo:
        json.dump(contenido, archivo, ensure_ascii=False,indent=4)


#datos = cargar_datos("datos.json")
#print (datos)
# Modificar algún dato
#datos[0]["edad"] = 29
#guardar_datos("datos_modificados.json", datos)


class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.nombre}, {self.edad} años, vive en {self.ciudad}"
    

#persona = Persona("Luis", 20, "Sevilla")
#print(persona)  # Luis, 20 años, vive en Sevilla
#print(persona.es_mayor_de_edad()) 

productos = [
    {"nombre": "manzana", "precio": 0.5, "cantidad": 50},
    {"nombre": "naranja", "precio": 0.8, "cantidad": 30},
    {"nombre": "pera", "precio": 0.75, "cantidad": 20},
    {"nombre": "platano", "precio": 0.4, "cantidad": 60}
]

def total_inventario(productos):
    total = 0
    for i in productos:
        total += i['precio'] * i['cantidad']

    return total

def producto_mas_caro(productos):
    masCaro = ""
    masMayor = 0
    for i in productos:
        if i['precio'] > masMayor:
            masMayor = i['precio']
            masCaro = i['nombre']

    return masCaro 

#print(total_inventario(productos))  # Debería devolver el valor total del inventario
#print(producto_mas_caro(productos))  # Debería devolver "naranja"

calificaciones = {
    "Ana": [90, 80, 85],
    "Carlos": [70, 75, 65],
    "Lucia": [88, 92, 84]
}

def promedio_calificaciones(calificaciones):
    nuevoDic = {}
    for estudiante, notas in calificaciones.items():
        promedio = sum(notas) / len(notas)
        nuevoDic[estudiante]=promedio
    return nuevoDic

def mejor_promedio(calificaciones):
    mejorEstudiante = ""
    mejorNota = 0
    aux = {}
    aux = promedio_calificaciones(calificaciones)
    for nombre, nota in aux.items():
        if nota > mejorNota:
            mejorNota = nota
            mejorEstudiante = nombre
    
    return mejorEstudiante

def añadir_estudiante(calificaciones, nombre, notas):
    calificaciones[nombre] = notas

def borrar_estudiante(calificaciones, nombre):
    if nombre in calificaciones:
        del calificaciones[nombre]
        print(f"Estudiante {nombre} eliminado.")
    else:
        print(f"Estudiante {nombre} no encontrado.")

def buscar_estudiante(calificaciones, nombre):
    if nombre in calificaciones:
        return calificaciones[nombre]
    else:
        return f"Estudiante {nombre} no encontrado."

