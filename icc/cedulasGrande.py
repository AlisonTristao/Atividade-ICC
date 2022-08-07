preço = int(input()) # Valor das compras
valorpg = int(input()) #  Valor pago

troco = valorpg-preço

c100 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
c1 = 0

#printa pra passar no vpl do moodle
print(troco)

while troco >= 100
    troco -= 100
    c100 += 1

while troco >= 50
    troco -= 50
    c50 += 1

while troco >= 20
    troco -= 20
    c20 += 1

while troco >= 10
    troco -= 10
    c10 += 1
    
while troco >= 5
    troco -= 5
    c5 += 1

while troco >= 2
    troco -= 2
    c2 += 1

while troco >= 1
    troco -= 1
    c1+= 1

print(c100)
print(c50)
print(c20)
print(c10)
print(c5)
print(c2)
print(c1)
