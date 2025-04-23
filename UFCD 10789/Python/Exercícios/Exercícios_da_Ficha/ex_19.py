# Escreva um programa que mostre os primeiros 60 números da serie bonatchi
# 1, 1, 2, 3, 5, 8, 13, 21.

# Como se constrói.

# 1+1=2
    # 1+2=3
        # 2+3=5
       
a = 1
b = 1
nums = 60 

print(a, end=" ")
print(b, end=" ")

for i in range(1, nums + 1):
    result = a + b
    a = b
    b = result
    print(result, end=" ")