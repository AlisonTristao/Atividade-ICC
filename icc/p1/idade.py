def idade(dia_n: int, mes_n: int, ano_n: int, dia_h: int, mes_h: int, ano_h: int):

    # compara se o dia é maior 
    if (mes_h > mes_n or (dia_h >= dia_n and mes_h == mes_n)) == False:
        if(ano_h == ano_n):
            # caso o dia seja menor e o ano é igual, o bb ainda n nasceu
            print(ano_h - ano_n)
        else:
            # se o dia for menor a criança ainda n fez aniversario
            print((ano_h - ano_n) -1)
    else:
        # calcula a idade apenas
        print(ano_h - ano_n)
    
dia_n = int(input()) # O dia de nascimento
mes_n = int(input()) # O mês de nascimento
ano_n = int(input()) # O ano de nascimento
dia_h = int(input()) # O dia de hoje
mes_h = int(input()) # O mês de hoje
ano_h = int(input()) # O ano de hoje

idade(dia_n, mes_n, ano_n, dia_h, mes_h, ano_h)
