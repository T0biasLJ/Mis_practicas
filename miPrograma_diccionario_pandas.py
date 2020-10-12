import pandas as pd

diccionario={}
lista=[]
lista2=[]
lista3=[]
for v in range(5):
    edad=int(input("dime las edades: "))
    e=lista.append(edad)
    diccionario["Edades"]=lista
    
for x in range(5):
    peso=int(input("cual es el peso: "))
    a=lista2.append(peso)
    diccionario["peso"]=lista2

for v in range(5):
    estatura=int(input("cual es tu estatura en cm: " ))
    b=lista3.append(estatura)
    diccionario["Estatura"]=lista3
    
diccionario2= pd.DataFrame(diccionario)
diccionario2.index= ["persona1","persona2","persona3","persona4","persona5"]
print(diccionario2)
  