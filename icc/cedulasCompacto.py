preço = int(input()) # Valor das compras
valorpg = int(input()) #  Valor pago

# calcula o troco
troco = valorpg-preço
print(troco)

valorCedulas = [100, 50, 20, 10, 5, 2, 1]
cedulas = [0, 0, 0, 0, 0, 0, 0]

# pra cada cedula
for m in range(len(valorCedulas)):
    # enquanto o troco ser maior q a cedula
    while troco >= valorCedulas[m]:
        # adiciona uma cedula 
        cedulas[m]+=1

        # diminui a cedula do troco
        troco -= valorCedulas[m]

# printa as cedulas
for m in cedulas:
    print(m)

