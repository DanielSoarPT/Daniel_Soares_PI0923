# Ler 10 números, e determinar se o número par e número impar.

num = 0
pares = []
impares = []

while num!= 10:
    try:
        inserir = int(input("Insira um numero: "))
    except ValueError:
        print("\nPor favor insira um numero valido.\n")
        continue
    
    if inserir % 2 == 0:
        pares.append(inserir)
    else:
        impares.append(inserir)
    num += 1
    
print("\nNumeros pares inseridos: ")
print(pares)

print("Numeros impares inseridos: ")
print(impares)