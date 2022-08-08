def validaHorário(hrs):
    # Aqui vai o seu código
    
    i = 1 # variavel que guarda o ciclo do for pra separar as datas
    # (acho que tem forma melhor de separar string, porem em python n sei)
    
    hh = "" # vai guardar as horas
    mm = "" # vai guardar os minutos 
    ss = "" # vai guardar os segundos

    zeros = 6-len(hrs)
    #  Quando digita um horario com 4 digitos ele nao tem horas (mm/ss)
    #  Entao se o horario tiver menos de 6 digitos significa q ele tem menos de 10hrs ou nao tem hora
    
    #  Entao adicionamos os zeros q faltam pra ele ficar com 6 digitos 
    #  Exemplo:
    #  a pessoa entrou com 4445 - significa 44 minutos e 45 segundos
    #  entao isso vai trasformar para 004445 - 00 horas 44 minutos e 45 segundos
    for j in range(zeros):
        hrs ="0"+hrs
    
    for m in hrs:
        #  e caso tenho os zeros negativos significa q a pessoa digitou mais de 6 digitos 
        #  tem esse if so pra pular os digitos antes (tem um exemplo que o professor botou um " "(espaço) antes e bugou tudo)
        
        if zeros >= 0:
            
            # caso esteja em 1 e 2 ele concatena os digitos em horas
            if i <=  2:
                hh += m
                
            # caso esteja entre 3 e 4 ele concatena os digitos em minutos
            elif i <= 4:
                mm += m
                
            #  senao ele vai estar entre 5 e 6 e concatena em segundos
            else:
                ss+= m
                
            #  no final de cada ciclo ele sona mais um no contador pra saber qual digito ele pegou ali
            i+=1
            
        else: 
            #  vai pulando os zeros e subtrai os q pulou aqui
            zeros += 1

    # print(hh, mm, ss)
    
    #  compara hora com hora minuto com minuto e sgundo com segundo
    if int(hh) > 23 or int(mm) > 59 or int(ss) > 59:
        return False

    return True

hrs = (input())
print(validaHorário(hrs))