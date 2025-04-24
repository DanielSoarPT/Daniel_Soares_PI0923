# Crie um algoritmo que mostre os 30 primeiros números ímpares e pares.

pares = []
impares = []

for num in range(1,61):
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
        
print("Os 30 primeiros numeros pares são: ")
print(pares)

print("Os 30 primeiros numeros impares são: ")
print(impares)