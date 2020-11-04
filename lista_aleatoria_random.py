import random

SEPARADOR=("*" * 40 + "\n")
lista=[]

while True:
    print("QUE DESEAS HACER")
    menu=int(input("1: Agregar numero a la lista, 2: Ver lista, 3: Elegir un numero aleatorio,4: Revolver la lista : \n"))
    print(SEPARADOR)
    if menu==1:
        op=int(input("1: Deseas agrgarlos tu 2: Agregar numeros aleatorios? \n"))
        if op==1:
            valores=int(input("Que numero deseas agregar"))
            X=lista.append(valores)
            print("Valores agregados")
            print(SEPARADOR)
        elif op==2:
            rango=int(input("Hasta que numero deseas agregar aleatoriamente"))
            a=random.randrange(rango)
            print(f"El numero aleatorio es {a}")
            agregado=lista.append(a)
            print("Numero agregado")
            print(SEPARADOR)
            
    elif menu==2:
        print(f"Esta es tu lista hasta ahora {lista} ")
        print(SEPARADOR)
    elif menu==3:
        aleatorio=random.choice(lista)
        print(f"Este es el numero aleatorio de la lista {aleatorio}")
        print(SEPARADOR)
    elif menu==4:
        barajada=random.shuffle(lista)#TENER EN CUENTA QUE AL REVOLVER LA LISTA NO SE REGRESARA A SU ESTADO ANTIGUO
        print(f"Esta es la nueva lista {barajada} ")
        print(SEPARADOR)
    elif menu==5:
        break

print("Gracias por usar el programa ")
    
        