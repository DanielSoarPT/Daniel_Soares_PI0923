# Crie um algoritmo que mostre os 30 primeiros números ímpares e pares.

pares = []
impares = []
num = 0

while num/2!=30:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    num += 1
        
print("Os 30 primeiros numeros pares são: ")
print(pares)

print("Os 30 primeiros numeros impares são: ")
print(impares)