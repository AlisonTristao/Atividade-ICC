A = []
B = []
C = []

# Leitura de A
for i in range(5):
    A.append(int(input())) 
# Leitura de B
for i in range(5):
    B.append(int(input()))

vetor = []
contador = 0
# salva a quantidade de vezes que o numero repete
for i in range(len(A)):
    for j in range(len(B)):
        if(A[i] == B[j]):
           vetor.append(int(A[i]));

C = A + B;
indexApagar = [];
qtdApagar = [];
# salva o idendex dos numeros repstidos
for i in range(len(C)):
    for j in range(len(vetor)):
        if C[i] == vetor[j]:
            indexApagar.append(vetor[j])

# exclui os numeros repetidos
for i in range(len(indexApagar)):
    C.remove(indexApagar[i]);


# pesquise sobnre conjuntos python no google
# que tem maneira mais facil de fazer isso

print(C);