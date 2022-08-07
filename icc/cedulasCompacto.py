preço = int(input()) # Valor das compras
valorpg = int(input()) #  Valor pago

troco = valorpg-preço
print(troco)

valorCedulas = [100, 50, 20, 10, 5, 2, 1]
cedulas = [0, 0, 0, 0, 0, 0, 0]

for m in range(len(valorCedulas)):
    while troco >= valorCedulas[m]:
        cedulas[m]+=1
        troco -= valorCedulas[m]

for m in cedulas:
    print(m)

