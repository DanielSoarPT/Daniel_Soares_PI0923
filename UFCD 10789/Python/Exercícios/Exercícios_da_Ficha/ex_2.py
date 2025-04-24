# Ler 10 números, e determinar se o número par e número impar.

pares = []
impares = []

for num in range(1, 11):
    try:
        inserir = int(input("Insira um numero: "))
    except ValueError:
        print("\nPor favor insira um numero valido.\n")
        continue
    
    if inserir % 2 == 0:
        pares.append(inserir)
    else:
        impares.append(inserir)
    
print("\nNumeros pares inseridos: ")
print(pares)

print("Numeros impares inseridos: ")
print(impares)