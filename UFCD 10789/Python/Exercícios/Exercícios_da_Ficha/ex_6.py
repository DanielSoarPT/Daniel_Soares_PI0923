# Crie um algoritmo que mostre os 10 primeiros números primos.

i = 0
j = 2 # Começa no 2, pois 1 não é um numero primo
numprim = []
    
while i <=10:
    if (j%2==0 and j!=2) or (j%3==0 and j!=3):
        j += 1
    else:
        numprim.append(j)
        j += 1
        i += 1
        
print(f"\nOs 10 primeiros numeros primos: {numprim}")