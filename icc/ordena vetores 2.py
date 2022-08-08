nome = ["Alison", "Cleber", "Joao", "Enzo", "Luquitas", "gustavo", "maria", "eduardo"]
nota = [7.0, 8.0, 6.5, 9.0, 6.0, 7.0, 7.5, 8.0]
nota2 = nota[:] # varial pra manipular e nao perder as notas reais
ordemVetores = [] # vai guardar a ordem dos index das notas
igual = [] # vai guardar o index das notas iguais

# ve quais variaveis são iguais e retira elas nas notas
def iguais(vetor):
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if i != j:
                if vetor[i] == vetor[j]:
                    igual.append(i) # salva o index das notas iguais

    for i in range(len(igual)):
        nota2.remove(nota[igual[i]]) # retira elas das notas

iguais(nota) # executa a funcão

# calcula a maior nota de um vetor
def maior(vetor):
    m = 0
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if i != j:
                if vetor[i] >= vetor[j]:
                    if m <= vetor[i]:
                        m = vetor[i]
            if len(vetor) == 1:
                m = vetor[0]
    return m

# calcula a maior nota do vetor e retira ela (repete ate nao ter mais nd no vetor)
for i in range(len(nota)):
    if(nota2 != []):
        maiorValor = maior(nota2)
        indexValor = nota.index(maiorValor)
        ordemVetores.append(indexValor)
        nota2.remove(maiorValor)

contador = 0 # guarda qual a volta q o loop esta pra poder verificar se alguma das iguais estão no meio
# printa na ordem
for i in ordemVetores:
    print("nome: ", nome[i], " - ", " nota: ", nota[i])
    for j in range(len(igual)): # verifica se alguma das iguais se encaixa no meio 
        if nota[igual[j]] < nota[i] and nota[igual[j]] > nota[ordemVetores[contador+1]]:
            print("nome: ", nome[igual[j]], " - ", " nota: ", nota[igual[j]])

    contador += 1
