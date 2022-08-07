def procura_palavra(palavra: str):
    # Aqui vai o seu código
    
    tabelaC = ""
    for i in tabela:
        for j in i:
            tabelaC += j
            
    #verifica se esta em alguma dessas linhas

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