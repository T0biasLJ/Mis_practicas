import pandas as pd

diccionario={}
diccionario2={}
print("*"*30,"Bievenido","*"*30)

personas=int(input("Cuantas personas vas a registrar : "))
lista_index=[]
opcion=1
while opcion==1:
    contador=1
    
    lista_edad=[]
    lista_estatura=[]
    lista_peso=[]
    lista_nombre=[]
    
    for persona in range(personas):
        nombre=(input(f"Dime el nombre {contador}: "))
        lista_nombre.append(nombre)
        listapersonas=[]
        edad=int(input("Dime tu edad : "))
        lista_edad.append(edad)
        estatura=float(input("Dime tu estatura : "))
        lista_estatura.append(estatura)
        peso=float(input("Dime tu peso : "))
        lista_peso.append(peso)
        contador=contador+1
        
        print("*"*30)
        
    diccionario2["Edades"]=lista_edad
    diccionario2["Estatura"]=lista_estatura
    diccionario2["Peso"]=lista_peso
    diccionario1=pd.DataFrame(diccionario2)

    
    for nombre in range(1,personas+1):
        diccionario1.index=[lista_nombre]

    
    opcion=2
    
    


print(diccionario1)