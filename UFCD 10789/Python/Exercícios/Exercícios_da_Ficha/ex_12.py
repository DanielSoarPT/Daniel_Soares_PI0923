# Elabore um programa que leia quantos números quer que se efetue a soma, subtrações, divisões, multiplicações e no
# fim por meio de um acumulador diga quantas operações foram efetuadas. Exemplo introduzindo o número 60 o programa deve
# apresentar 60 a somar, dividir multiplicar e subtrair por todos os números menores que ele.

while True:
    try:
        print("Insira um numero")
        num = int(input(">> "))
        print()
    except ValueError:
        print("\nInsira um valor valido\n")
        continue

    for i in range(1, num):
        print(f"{num} + {i} = {num + i}")
        print(f"{num} - {i} = {num - i}")
        print(f"{num} * {i} = {num * i}")
        print(f"{num} / {i} = {num / i}")
        print()

    break