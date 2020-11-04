import openpyxl
import random

libro= openpyxl.Workbook() #Creacion del libro
hoja= libro["Sheet"] #hoja

print("*" * 20,"Hola","*" * 20)

while True:
    print("Que deseas hacer: ")
    menu= int(input("1:sumar cantides\n2:Salir\n"))
    if menu == 1:
        nombre= input("Como deseas que se llame la hoja de tu libro: \n") #Pedimos al usuario como quiere que se llame su hoja
        hoja.title= nombre
        rango= int(input("Hasta que renglon quieres llegar: "))
        hoja["B1"].value= "Listado Random"
        for renglon in range(2,rango+1):#se empieza por el 2 ya que en hoja["B1"].value se le da la primera celda a empezar
            hoja.cell(row=renglon, column=2).value = random.randrange(100)
        string=str(rango)
        funcion="=SUM"
        funcion2="(B2:"
        funcion3="B"
        funcion4=")"
        fin=funcion+funcion2+funcion3+string+funcion4
        hoja["D9"].value="Suma"
        hoja["E9"].value=fin
        
        
        
    break
libro.save("Prom.xlsx")
print("Libro creado exitosamente!")
       
    
    


