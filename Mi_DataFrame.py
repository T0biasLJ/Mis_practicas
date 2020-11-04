import pandas as pd

diccionario={}
lista_nombre=[]
lista_materia=[]
lista_calif=[]
SEPARADOR=("*"* 40 + "\n")
print("*"*30,"bienvenido","*"*30)

while True:
    print("QUE DESEAS HACER: ")
    menu=int(input("1:Registrar alumnos, 2:Ver Datos,3:Exportar a csv, 4:Salir \n"))
    if menu == 1:
        alumnos=int(input("Cuantos alumnos vas a registrar: \n"))
        for alumno in range(alumnos):
            nombre=input("Nombre del alumno: \n")
            lista_nombre.append(nombre)
            materia=input("Nombre de la materia: \n")
            lista_materia.append(materia)
            calificacion=int(input("Cual es la calificacion: \n"))
            lista_calif.append(calificacion)
        
        diccionario["Materias"]=lista_materia
        diccionario["Calificacion"]=lista_calif
        diccionario1= pd.DataFrame(diccionario)
        
        for nombre in range(1,alumnos+1):
            diccionario1.index=[lista_nombre]
        
        print("Proceso Realizado")
        print(SEPARADOR)
        
    elif menu== 2:
        print(diccionario1)
        print(SEPARADOR)
    elif menu== 3:
        diccionario1.to_csv(r'diccionario1.csv',index=True,header=True)
        print("EXITO")
        print(SEPARADOR)
    
    elif menu== 4:
        break