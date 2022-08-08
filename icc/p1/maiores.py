def calculaMaior(a, b, c, d, e):

    # lista com os numeros
    lista = [a, b, c, d, e]

    # recebe o maior
    max1 = max(lista)

    # remove ele
    lista.remove(max1)

    # calcula o segundo maior
    max2 = max(lista)

    # printa os maiores
    print(max1)
    print(max2)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

calculaMaior(a, b, c, d, e)
