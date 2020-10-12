import random
listaR=[]
listag=[]
listaL=[]
for v in range(2):
    r=random.randrange(6,12)
    listaR.append(r)
for x in range(2):
    g=random.randrange(6,12)
    listag.append(g)
for y in range(2):
    l=random.randrange(6,12)
    listaL.append(l)

print(f"numero de problemas para ricardo: {listaR}")
print(f"numero de problemas para Gera: {listag}")
print(f"numero de problemas para Luis: {listaL}")