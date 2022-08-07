n = int(input(""))
nota1 = []
for i in range(n):
    nota1.append(int(input("")))

notas = [0, 0, 0, 0, 0]

media = 0
for i in notas:
    media += i
    
media = media/len(nota1)

for i in range(len(nota1)):
    if media >= 9.0:
        notas[0] += 1 
    elif media >= 8.0:
        notas[1] += 1 
    elif media >= 7.0:
        notas[2] += 1 
    elif media >= 6.0:
        notas[3] += 1 
    else:
        notas[4] += 1 
        
for i in range(5):
    for j in range(notas[i]):
        print("#")
        
    print("\n")