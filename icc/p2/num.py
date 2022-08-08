def pegaDígito(numero: int, posicao: int):
    # Aqui vai o seu código
   
    # trasforma o numero em string
    strNum = str(numero)
    # pega o niumero pelo index ao contrario
    contador = len(strNum) - posicao
   
    # quando o contador ser zerar ele printa o numero
    for i in strNum:
        contador -= 1
        if contador == 0:
            return i
    

# Aqui a função é chamada
x = int(input())
p = int(input())
print(pegaDígito(x, p))