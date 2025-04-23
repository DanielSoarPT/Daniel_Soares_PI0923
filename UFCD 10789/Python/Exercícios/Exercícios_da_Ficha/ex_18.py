# Elabore um programa que leia uma entrada e diga quantos números perfeitos existem.
# Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial.

divisores = []

while True:
    try:
        num = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Insira um numero valido")
        continue

    for i in range(1, num - 1):
        if (num % i == 0):
            divisores.append(i)
    
    if sum(divisores) == num:
        print(f"\nO numero é perfeito | Divisores: {divisores} | Soma dos divisores: {sum(divisores)}\n")
    else:
        print(f"\nO numero não é perfeito | Divisores: {divisores} | Soma dos divisores: {sum(divisores)}\n")
        
    break
    