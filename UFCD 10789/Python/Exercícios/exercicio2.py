num = int(input("Insira um numero: "))

if (num%2==0 and num!=2) or (num%3==0 and num!=3):
    print("Número não é primo")
else:
    print("Número é primo")