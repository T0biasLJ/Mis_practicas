import random
import time

SEPARADOR= ("-" *30) + "\n"
caras=int(input("dime un numero de caras para el dado: "))
print(f"el numero de caras elegido es {caras} \n")
horaInicial= time.time()

while True:
    r=input("enter para sacar un numero aleatorio...(* para salir))")
    if r =='':
        aleatorio= random.randrange(caras +1)
        print(f"el numero aleatorio es {aleatorio}\n")
        print(SEPARADOR)
    elif r == "*":
        break
print(SEPARADOR)
duracion= round(time.time() - horaInicial, 2)
print(f"el proceso tardo {duracion} segundos")