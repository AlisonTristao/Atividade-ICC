import statistics #importação da biblioteca q tem o desvio padrao

livros = [{'nome':'alison', 'preço':7.0}, {'nome':'joao', 'preço':8.0}, {'nome':'enzo', 'preço':6.0}, {'nome':'cleber', 'preço':10.0}]

media = 0.0
vetorPrecos = []
#soma o preço de todos
for i in range(len(livros)):
    media += livros[i]['preço']
    #cria um vetor pra caluclar o desvrio padrao (aproveitei o for pra nao fazer outro igual)
    vetorPrecos.append(livros[i]['preço'])

#divide a soma pela quantidade
media = media/len(livros)

print("livros acima da media:")
for i in range(len(livros)):
    #se o preço ser maior q a media printa
    if livros[i]['preço'] > media:
        print(livros[i])

#retorna o preço de cada livro pra usar no metodo.sort()
def maior(e):
    return e['preço']

#ordena do menor pro maior
livros.sort(key=maior)

#lista igual tirando do primeiro elemento em diante (menos o menor)
novaLista = livros[1:]

#ordena do maior pro menor
novaLista.sort(reverse=True, key=maior)

#adiciona o menor no começo da lista
novaLista.insert(0, livros[0])

#desvio padrao (esse é o Desvio padrão populacional dos dados.)
#tem tbm o Desvio padrão amostral dos dados. stdev()
# caso sej a o outro é so mudar de pstdev para stdev()
desvio = statistics.pstdev(vetorPrecos)

print("Lista com menor na frente: \n", novaLista)
print("desvio padrão dos preços: ", desvio)

