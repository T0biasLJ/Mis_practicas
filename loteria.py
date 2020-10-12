"Loteria"
import random
cartas={1:"El gallo",2:"El diablo",3:"El catrin",4:"El paraguas",
        5:"La sirena",6:"La escalera",7:"La botella",8:"El barril",
        9:"El arbol",10:"El melon"}

contador=1
lista_numeros= list(cartas.keys())

while True:
    respuesta=input("Presiona enter para jugar, (*) para salir: ")
    if respuesta=="":
        random.shuffle(lista_numeros)
        for carta in lista_numeros:
            print(f"la carta numero {contador} es {cartas[carta]}")
            contador+=1
            respuesta2=input("Quieres otra carta?: ")
            if respuesta2=="No" or respuesta2=="no":
                print("Okey")
                break
    break

print("GRACIAS POR JUGARS")
                
            
        
    