# Elabore um programa que leia um número e mostre a tabuada. (multiplicar de 1 a 10)

while True:
    try:
        print("Insira um numero")
        num = int(input(">> "))
        print()
    except ValueError:
        print("\nInsira um valor valido\n")
        continue

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

    break