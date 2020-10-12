import random

otra= True
respuesta= "X"
cartas={1:"El gallo",2:"El diablo",3:"El catrin",4:"El paraguas",
        5:"La sirena",6:"La escalera",7:"La botella",8:"El barril",
        9:"El arbol",10:"El melon"}
lista_numeros= list(cartas.keys())
pass

random.shuffle(lista_numeros)

opcion=input("QUIERES JUGAR?: ")
print("CORRE Y SE VA CORRIENDO CON: ")

if opcion=="si":
    for carta in lista_numeros:
        print(cartas[carta])
        respuesta= input("Otra carta?: ")
        if respuesta== "N" or respuesta == "n":
            otra== False
            break
if opcion=="no":
    pass
    

print("Gracias por jugar")
    
