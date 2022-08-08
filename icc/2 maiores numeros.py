def maiores(a, b, c, d, e):
    # codigo aqui

    # array que vai ter os valores para ficar mais facil de usar no metodo for
    array = [a, b, c, d, e]

    # variavel q vai possuir o valor maximo (max() já faz automatico)
    maximo1 = max(array)

    # remove o maior (nao consegui usar o .remove() pq acho q nessa versão n deve funcionar)
    array.pop(array.index(maximo1))

    # calcula o segundo maior
    maximo2 = max(array)
    # se eles forem iguais temos q tirar o terceiro
    if maximo2 == maximo1:
        # vai repetir ate n ter iguais (caso tenha 3, 4 ou 5) 
        while maximo2 == maximo1:
            # retira o valor igual
            array.pop(array.index(maximo2))
            # calcula o maior de novo
            maximo2 = max(array)

    # se der 5 valores iguais da erro
    print(maximo1)
    print(maximo2)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

maiores(a, b, c, d, e)
