def validaHorário(hrs):
    # Aqui vai o seu código
    
    i = 1
    hh = ""
    mm = ""
    ss = ""

    zeros = 6-len(hrs)

    for j in range(zeros):
        hrs ="0"+hrs
    
    for m in hrs:
        if zeros >= 0:
            if i <=  2:
                hh += m
            elif i <= 4:
                mm += m
            else:
                ss+= m
            i+=1
        else: 
            zeros += 1

    print(hh, mm, ss)
    
    if int(hh) > 23 or int(mm) > 59 or int(ss) > 59:
        return False

    return True

hrs = (input())
print(validaHorário(hrs))
