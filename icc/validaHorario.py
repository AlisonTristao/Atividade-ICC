def validaHorário(hrs):
    # Aqui vai o seu código

    #nao funcionou pois entrega valores com menos de 6 digitos

    vetorHrs = []
   
    for i in hrs:
       vetorHrs.append(i)

    hh = vetorHrs[0] + vetorHrs[1]
    mm = vetorHrs[2] + vetorHrs[3]
    ss = vetorHrs[4] + vetorHrs[5]

    if (int(hh)) > 23 or (int(mm)) > 59 or (int(ss)) > 59:
        return False

    return True

hrs = (input())
print(validaHorário(hrs))
