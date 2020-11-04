import openpyxl
import random



class datos:
    def __init__(self,cuantos,rango,nombre):
        self.__cuantos=cuantos
        self.__rango=rango
        self.__nombre=nombre
        
    
    def creacion(self):
        libro=openpyxl.Workbook()
        hoja=libro["Sheet"]
        hoja.title="NumerosRandom"
        hoja["B1"]="Numero Aleatorios"
        
        for renglon in range(2,self.__cuantos+2):
            hoja.cell(row=renglon,column=2).value= random.randrange(self.__rango)
            
        print("Menu de operaciones ")
        print("1=Sumar\n2=Promedio\n3=AMBAS\n4=No quiero ninguna operacion extra")
        opcion=int(input(": "))
        if opcion==1:
            string=str(self.__cuantos+1)
            funcion="=SUM"
            funcion2="(B2:"
            funcion3="B"
            funcion4=")"
            fin=funcion+funcion2+funcion3+string+funcion4
            hoja["D9"].value="Suma"
            hoja["D10"].value=fin
            nombre2=".xlsx"
            nombref=self.__nombre+nombre2
            libro.save(nombref)
            print("EXITOSO")
        
        elif opcion==2:
            string=str(self.__cuantos+1)
            funcion="=PROMEDIO"
            funcion2="(B2:"
            funcion3="B"
            funcion4=")"
            fin=funcion+funcion2+funcion3+string+funcion4
            hoja["E9"].value="Promedio"
            hoja["E10"].value=fin
            nombre2=".xlsx"
            nombref=self.__nombre+nombre2
            libro.save(nombref)
            print("EXITOSO")
            
        elif opcion==3:
            string=str(self.__cuantos+1)
            funcion="=SUM"
            funcion2="(B2:"
            funcion3="B"
            funcion4=")"
            fin=funcion+funcion2+funcion3+string+funcion4
            hoja["D9"].value="Suma"
            hoja["D10"].value=fin
            
            funcion5="=PROMEDIO"
            funcion6="(B2:"
            funcion7="B"
            funcion8=")"
            fina=funcion5+funcion6+funcion7+string+funcion8
            hoja["E9"].value="Promedio"
            hoja["E10"].value=fina
            nombre2=".xlsx"
            nombref=self.__nombre+nombre2
            libro.save(nombref)
            print("EXITOSO")
        
        elif opcion==4:
            nombre2=".xlsx"
            nombref=self.__nombre+nombre2
            libro.save(nombref)
            print("EXITOSO")
            
        
       
            
            
        
    


opcion1=1
while opcion1==1:
    cuantos=int(input("Dime cuantos numero aleatorios quieres en tu Excel : "))
    rango=int(input("Dime el ultimo numero permitido de numero aleatorios : "))
    nombre=input("Como quieres que se llame el Excel : ")
    objeto=datos(cuantos,rango,nombre)
    objeto.creacion()
    print("*"*50)
    print("1=SI\n2=No")
    opcion1=int(input("Deseas seguir creando excel : "))
    print("*"*50)
    