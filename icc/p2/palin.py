def souPalíndromo(n):
# Aqui vai o seu código

    #vai guardar o resultado sem espaço
    result = ""
    
    #igual o texto fornecido sem espaço
    for i in n:
        if i != " ":
           result += i 
    
    #variavel ao contrario
    contrario = result[::-1]
    
    #retorn true ou false
    return contrario == result

# Programa principal (não modifique nada)

n = input()
n = n.lower()

if souPalíndromo( n ):
   print("Palíndroma")
else:
   print("Não palíndroma")