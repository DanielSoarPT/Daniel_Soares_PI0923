# Elabore um programa que constitua a média de 30 números pares que sejam introduzidos. Validando a entrada de números inteiros entre 1 e 50.

nums = []

for i in range(30):
    while True:
        try:
            print("\nInsira um número par entre 1 e 50")
            num = int(input(">> "))

            if num < 1 or num > 50:
                print("\nO número tem que ser entre 1 e 50")
            elif num % 2 != 0:
                print("\nO número tem que ser par")
            else:
                nums.append(num)
                print(f"\nNúmero {num} adicionado.")
                break

        except ValueError:
            print("\nInsira um valor válido\n")

media = sum(nums) / len(nums)
print(f"Média: {media:.2f}")