def totalEnvelopes(RS, PE, PS, QS, QE):

    #se for 0 de dinheiros retorna apenas oq ele tem
    if(RS == 0):
        return int(min(QS, QE))
    else:
        #calcula o quanto que faltaComprar pra ele comprar
        faltaComprar = 0
        if QS > QE:
            faltaComprar = (QS-QE)*PE
        elif QE > QS:
            faltaComprar = (QE-QS)*PS

        #valor de dinheiro que vai sobrar
        valorSobra = RS-faltaComprar
        
        #se o valor que sobra ser negativo ele tem menos dinheiro do que ele precisa comprar
        if(valorSobra < 0):
            #conta um por um quantos ele consegue comprar ate o dinheiro acabar
            #caso precise de selos
            if QS > QE:
                while QS >= QE and RS > 0:
                    RS -= PS
                    QE += 1
            #caso precise de envelopes
            elif QE > QS:
                while QE >= QS and RS > 0:
                    RS -= PE
                    QS += 1
            #retorna oq ele conseguiu comprar
            return int(min(QS, QE))
        
        #se o valor ser positivo ele divide pelo preço 
        cartas = (RS-faltaComprar)//(PE+PS)
        
        #retorna o quanto conseguiu comprar mais o quanto tinha
        return int((cartas)+max(QS, QE))  

RS = float(input()) #dinheiro
PE = float(input()) #preço do envelope
PS = float(input()) #preço do selo
QS = float(input()) #quantidade de selos q ele ja tem
QE = float(input()) #quantidade de envelopes q ele ja tem

print(totalEnvelopes(RS, PE, PS, QS, QE))
