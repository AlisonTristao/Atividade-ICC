A = []
B = []
C = []

#Leitura de A
for i in range(5):
    A.append(int(input())) 
# Leitura de B
for i in range(5):
    B.append(int(input()))

# Criação de C
vetor = []
contador = 0
for i in range(len(A)):
    for j in range(len(B)):
        if(A[i] == B[j]):
           vetor.append(int(A[i]));

C = A + B;
indexApagar = [];
qtdApagar = [];
for i in range(len(C)):
    for j in range(len(vetor)):
        if C[i] == vetor[j]:
            indexApagar.append(vetor[j])
            
for i in range(len(indexApagar)):
    C.remove(indexApagar[i]);

print(C);