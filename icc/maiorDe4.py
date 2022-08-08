def maiorDe4(a, b, c, d):
    # Aqui vai o seu código  
    if a > b and a > c and a > d:
        return a
    elif b > c and b > d:
        return b
    elif c > d:
        return c
    else:
        return d
        
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
maior = maiorDe4(n1, n2, n3, n4)
print(maior)
