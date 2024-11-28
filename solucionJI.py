# Pregunta 1: JSON - Cargar y Guardar Datos
import json

def cargar_datos(fichero):
    with open(fichero, 'r') as archivo:
        datos = json.load(archivo)
    return datos

def guardar_datos(fichero, datos):
    with open(fichero, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
        
# Ejemplo de uso
datos = cargar_datos("datos.json")
datos[0]["edad"] = 29
guardar_datos("datos_modificados.json", datos)

# Pregunta 2: Orientación a Objetos
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años, vive en {self.ciudad}"
        
# Ejemplo de uso
persona = Persona("Luis", 20, "Sevilla")
print(persona)  # Luis, 20 años, vive en Sevilla
print(persona.es_mayor_de_edad())  # True

#Pregunta 3: Diccionarios y Listas
productos = [
    {"nombre": "manzana", "precio": 0.5, "cantidad": 50},
    {"nombre": "naranja", "precio": 0.8, "cantidad": 30},
    {"nombre": "pera", "precio": 0.75, "cantidad": 20},
    {"nombre": "platano", "precio": 0.4, "cantidad": 60}
]

def total_inventario(productos):
    return sum(producto["precio"] * producto["cantidad"] for producto in productos)

def producto_mas_caro(productos):
    producto_caro = max(productos, key=lambda producto: producto["precio"])
    return producto_caro["nombre"]

# Ejemplo de uso
print(total_inventario(productos))  # Valor total del inventario
print(producto_mas_caro(productos))  # "naranja"

# Pregunta 4: Manipulación de Diccionarios
calificaciones = {
    "Ana": [90, 80, 85],
    "Carlos": [70, 75, 65],
    "Lucia": [88, 92, 84]
}

def promedio_calificaciones(calificaciones):
    promedios = {}
    for estudiante, notas in calificaciones.items():
        promedios[estudiante] = sum(notas) / len(notas)
    return promedios

def mejor_promedio(calificaciones):
    promedios = promedio_calificaciones(calificaciones)
    estudiante_mejor = max(promedios, key=promedios.get)
    return estudiante_mejor

def añadir_estudiante(calificaciones, nombre, notas):
    calificaciones[nombre] = notas

def borrar_estudiante(calificaciones, nombre):
    if nombre in calificaciones:
        del calificaciones[nombre]
    else:
        print(f"El estudiante {nombre} no se encontró en el registro.")

def buscar_estudiante(calificaciones, nombre):
    if nombre in calificaciones:
        return calificaciones[nombre]
    else:
        return f"El estudiante {nombre} no existe en el registro."

# Ejemplo de uso
print(promedio_calificaciones(calificaciones))  # {'Ana': 85.0, 'Carlos': 70.0, 'Lucia': 88.0}
print(mejor_promedio(calificaciones))           # 'Lucia'
añadir_estudiante(calificaciones, "Jorge", [75, 80, 78])
print(calificaciones)                           # Debería incluir a "Jorge" con sus notas
borrar_estudiante(calificaciones, "Carlos")
print(calificaciones)                           # Debería haber eliminado a "Carlos"
print(buscar_estudiante(calificaciones, "Ana")) # Debería mostrar la lista de calificaciones de Ana
print(buscar_estudiante(calificaciones, "Carlos")) # Debería mostrar un mensaje indicando que no existe