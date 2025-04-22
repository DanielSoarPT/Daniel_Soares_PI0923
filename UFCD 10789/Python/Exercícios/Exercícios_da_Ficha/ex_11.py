# Elabore um ciclo for para produzir o seguinte output.
#	1
#	22
#	333
#	4444
#	55555

while True:
    try:
        print("Insira um numero")
        num = int(input(">> "))
        print()
    except ValueError:
        print("\nInsira um numero valido\n")
        continue

    for i in range(1,num+1):
        for j in range(1, i+1):
            print(i, end="")
        print()
    
    break