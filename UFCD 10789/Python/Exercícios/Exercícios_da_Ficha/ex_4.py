# Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não.
try:
    num = int(input("Insira um numero: "))
except ValueError:
    print("\nPor favor insira um numero valido.\n")

if (num%2==0 and num!=2) or (num%3==0 and num!=3):
    print("Número não é primo")
else:
    print("Número é primo")