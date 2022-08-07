def diasPassados(d, m, a):
    
    #quantidade de dias de cada mes
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #variavel q vai somar os dias
    diasTotais = 0;

    #em ano bi fevereiro recebe 29
    if a%4 == 0:
       meses[1] = 29

    #diminui o ultimo mes pra somar so os dias 
    m -= 1

    #soma todos os meses menos o atual
    for mes in range(m):
        diasTotais += meses[mes]

    #soma com os dias q faltam do mes atual
    diasTotais += d

    #retorna os dias totais
    return diasTotais 

d = int(input())
m = int(input())
a = int(input())
print(diasPassados(d, m, a))
