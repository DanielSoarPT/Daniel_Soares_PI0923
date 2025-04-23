# Elabore um programa que determine os múltiplos de 5 mas não múltiplos de 3 …. De 1 a 1000 deve ser a sequência.

for i in range(1, 1001):
    if i % 5 == 0 and i % 3 != 0:
        print(f"{i}")