def imposto_renda(nro_horas, valor_h, nro_filhos):
    # Aqui vai o código da função que você deve escrever
    
    salario = (nro_horas*valor_h) - 189.59*nro_filhos
    IR = 0
    desc = 0
    
    if salario <= 1903.98:
        IR = 0
    elif salario <= 2826.65:
        IR = 7.5
        desc = 142.8
    elif salario <= 3751.05:
        IR = 15
        desc = 354.80
    elif salario <= 4664.68:
        IR = 22.5
        desc = 636.13
    else:
        IR = 27.5
        desc = 869.36
    
    IR = (IR/100)*salario - desc
    return IR
    
# Programa Principal
nro_horas = int(input())
valor_h = float(input())
nro_filhos = int(input())
ir = imposto_renda(nro_horas, valor_h, nro_filhos)



ir_formatado = "{:.2f}".format(ir)
print(ir_formatado)
