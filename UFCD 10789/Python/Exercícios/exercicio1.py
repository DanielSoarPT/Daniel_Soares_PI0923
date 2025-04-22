num1 = 114
num2 = 86
num3 = 94

if num1>num2 and num2>num3:
    print("Num1 é maior, Num2 está no meio e o num3 é o menor")
elif num1>num3 and num3>num2:
    print("Num1 é maior, Num3 está no meio e o num2 é o menor")
elif num3>num2 and num2>num1:
    print("Num3 é maior, Num2 está no meio e o num1 é o menor")
elif num3>num1 and num1>num2:
    print("Num3 é maior, Num1 está no meio e o num2 é o menor")
elif num2>num1 and num1>num3:
    print("Num2 é maior, Num1 está no meio e o num3 é o menor")
elif num2>num3 and num3>num1:
    print("Num2 é maior, Num3 está no meio e o num1 é o menor")