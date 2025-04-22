# Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não.

while True:
    try:
        num = int(input("Insira um numero (Insira 0 para sair): "))
    except ValueError:
        print("\nPor favor insira um numero valido.\n")
        continue

    if num == 0:
        print("\nAdeus")
        break

    if (num%2==0 and num!=2) or (num%3==0 and num!=3):
        print("\nNúmero não é primo\n")
    else:
        print("\nNúmero é primo\n")