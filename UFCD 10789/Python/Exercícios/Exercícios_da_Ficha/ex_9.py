# Escreva um programa que solicite um número ao utilizador até que o valor deste esteja entre os valores 1 e 100. (Use o ciclo do ... while)

i = True

while i == True:
    try:
        print("Insira um numero")
        num = int(input(">> "))
    except ValueError:
        print("\nInsira um numero valido!\n")
        continue

    while num < 1 or num > 100:
        print("\nO numero tem que estar entre os valores 1 e 100.\n")
        break

    if num >= 1 and num <=100:
        i = False
        print("\nO valor esta entre 1 e 100.\n")