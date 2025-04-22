# Altere o programa anterior para que mostre todas as tabuadas de 1 a 100. (ciclos for).

for i in range(1, 101):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()