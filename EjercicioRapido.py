lista = [5,15,20,35]
lista2 = [{"Nombre":"JI","Edad":34},
          {"Nombre":"MI","Edad":20},
          {"Nombre":"MI","Edad":17}]
def promedio(lista):
    sumaTotal = 0
    divTotal = len(lista)
    for i in lista:
        sumaTotal+=i
    
    resultado = sumaTotal/divTotal
    print(resultado)

def suma(lista):
    sumaTotal = 0
    for i in lista:
        sumaTotal+=i
    
    print(suma)     

def mayor10(lista):
    listanueva = []
    for i in lista:
        if i > 10:
            listanueva.append(i)
    
    print(listanueva)

media_edad = sum(d["Edad"] for d in lista2) / len(lista2)
mayor_edad = sum(d["Edad"] for d in lista2 if d["Edad"] >= 18) / len(lista2)

suma(lista)
promedio(lista)
mayor10(lista)
print(sum(i for i in lista if i > 10))
print(min(i for i in lista if i > 10))
print(media_edad)