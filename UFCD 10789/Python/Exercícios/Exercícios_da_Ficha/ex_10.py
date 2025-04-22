# Elabore um programa que lê um número e escreve quantos divisores ele possui.

divisores = []

while True:
    try:
        num = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Insira um numero valido")
        continue

    for i in range(1, num + 1):
        if (num % i == 0):
            divisores.append(i)

    print(f'O números de divisores: {divisores}')

    break