def procura_palavra(palavra: str):
    # Aqui vai o seu código
    
    # guarda as linhas na vertical
    vertical = ""
    
    # guarda as linhas na horizontal
    horizontal = ""
    
    # junta tudo em uma linha so horizontal e vertical
    for i in range(len(tabela)):
        for j in range(len(tabela[i])):
            horizontal += tabela[i][j]
            vertical += tabela[j][i]
            
    # verifica se esta em alguma dessas linhas
    if palavra in vertical:
        return True
    elif palavra in horizontal: 
        return True
    else: 
        return False # senao retoan false

tabela = [
 ['A', 'T', 'O', 'L', 'E', 'P', 'S', 'J'],
 ['B', 'J', 'L', 'U', 'T', 'M', 'S', 'I'],
 ['A', 'I', 'U', 'R', 'O', 'U', 'P', 'A'],
 ['C', 'L', 'T', 'S', 'M', 'A', 'T', 'E'], 
 ['A', 'J', 'L', 'O', 'A', 'R', 'M', 'A'],
 ['T', 'J', 'L', 'O', 'T', 'M', 'S', 'I'],
 ['E', 'J', 'L', 'V', 'E', 'M', 'S', 'I'],
 ['T', 'J', 'L', 'O', 'T', 'I', 'M', 'E'],
 ]

palavra = input()
palavra = palavra.upper()
print(procura_palavra(palavra))