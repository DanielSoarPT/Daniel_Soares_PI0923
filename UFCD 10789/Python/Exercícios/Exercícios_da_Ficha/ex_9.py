# Escreva um programa que solicite um número ao utilizador até que o valor deste esteja entre os valores 1 e 100. (Use o ciclo do ... while)

while True:
    try:
        print("Insira um numero")
        num = int(input(">> "))
    except ValueError:
        print("\nInsira um numero valido!\n")
        continue

    if num >= 1 and num <=100:
        print("\nO valor esta entre 1 e 100.\n")
        break
    else:
        print("\nO numero não esta entre 1 e 100.\n")