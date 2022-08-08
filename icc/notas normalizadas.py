n=int(input("")) 

list_normalizada=[]
lis_cod=[]
lis_not=[]
c=0
listaFinal=[]

# recebe a lista de notas e a lista do cod delas
while c<n:
    cod=int(input(""))
    nota=float(input(""))
    lis_cod.append(cod)
    lis_not.append(nota)
    c=c+1

# normaliza as notas
for i in lis_not:
    normalizada=(i*10)/max(lis_not)
    norm=round(normalizada,2)
    list_normalizada.append(norm)

# adciona na lista
for j in range(n):
    listaFinal.append(([lis_cod[j]] + [list_normalizada[j]])) 

print(listaFinal)