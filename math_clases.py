import math

class Operacion:
    def __init__(self,numero):
        self.__numero=numero
    
    def floor(self):
        a=math.floor(self.__numero)
        return f"{a}"
    
    def ceil(self):
        b=math.ceil(self.__numero)
        return f"{b}"
    
    def raiz(self):
        c=math.sqrt(self.__numero)
        return f"{c}"
    
    def factor(self):
        d=math.factorial(self.__numero)
        return f"{d}"
    
    def potencia(self):
        pot=int(input("A que potencia lo quieres elevar"))
        e=math.pow(self.__numero,pot)
        return f"{e}"
    
    
    
SEPARADOR=("-"*40 + "\n")


while True:
    
    print("ESTE PROGRAMA AYUDA A ELEVAR,DISMINUIR UN ENTERO,OBTENER RAIZ CUADRADA,FACTORIAL Y POTENCIAS")
    print(SEPARADOR)
    
    n=float(input("Dame un numero: ")) #Pedimos un nuemro al usuario
    print(SEPARADOR)
    print("QUE DESEAS HACER")
    menu=int(input("""1:Elevar numero hacia arriba,2:Llevar el numero hacia abajo,3: Obtener la raiz cuadrada del numero,
4: Obtener el factorial, 5: Potenciar numero, 6:SALIR : """))
    
    print(SEPARADOR)
    #Comienza el menu "if"
    if menu==1:
        x=Operacion(n)
        y=x.ceil()
        print(f"El entero hacia arriba de {n} es {y}")
        print(SEPARADOR)
    
    elif menu==2:
        x=Operacion(n)
        y=x.floor()
        print(f"El entero hacia abajo de {n} es {y}")
        print(SEPARADOR)
        
    elif menu==3:
        x=Operacion(n)
        y=x.raiz()
        print(f"La raiz del numero {n} es de {y}")
        print(SEPARADOR)
        
    elif menu==4:
        x=Operacion(n)
        y=x.factor()
        print(f"El factorial del numero {n} es de {y}")
        print(SEPARADOR)
        
    elif menu==5:
        x=Operacion(n)
        y=x.potencia()
        print(f"El numero {n} elevado a la potencia dada es {y} ")
        print(SEPARADOR)
        
    elif menu==6:
        break
print("Gracias por usar el programa :3")
    
    