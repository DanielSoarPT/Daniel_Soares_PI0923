# Elabore um programa que leia um valor de entrada e mostre para cada valor até ao 1
# (se é número Primo, Quantos divisores e números perfeitos) o Programa deve validar entradas entre 1 e 30.000,
# e parar de 10 em 10 valores com instrução para parar ou continuar. No mesmo programa use um menu e
# Elabore uma calculadora simples (+,-,*,/) com a função extra tabuada.
# Validar entradas de 1 a 1000 (nota a tabuada deve apresentar todas as multiplicações de 1 ate ao máximo introduzido)
# deve parar de 20 em 20 valores.

import os

def clear():
    os.system("cls")

while True:
    print("\n+ MENU +\n\n[1] - Mostrar cada valor até ao 1 de um número\n[2] - Calculadora\n[0] - Sair")
    esc = input(">> ")

    if esc == '1':
        clear()
        ligado = True
        while ligado:
            try:
                print("Insira um valor inteiro entre 1 e 30000.\n")
                num = int(input(">> "))
            
                if num < 1 or num > 30000:
                    clear()
                    print("O número tem que estar entre 1 e 30000.\n")
                    continue
                
                print("\n------------------\n")
                
                divs = []
                
                if (num%2==0 and num!=2) or (num%3==0 and num!=3):
                    print(f"O número {num} não é primo.")
                else:
                    print(f"O número {num} é primo.")
                    
                for i in range(1, num - 1):
                    if (num % i == 0):
                        divs.append(i)
                        
                if sum(divs) == num:
                    print(f"O número {num} é perfeito.")
                else:
                    print(f"O número {num} não é perfeito.")
                    
                if divs:
                    print(f"O número {num} tem {len(divs)} divisores, eles sendo: {divs}.")
                else:
                    print(f"O número {num} não tem divisores.")
                    
                print("\n------------------\n")
                
                contador = 0
                
                for i in range(num, 0, -1):
                    print(i)
                    contador += 1
                    if i == 1:
                        break
                    if contador == 10:
                        print("\nPressione no enter (ou qualquer caracter) para continuar. Se quiser sair, insira um 'S'.")
                        cont = input(">> ")
                        print("")
                        if cont == 's' or cont == 'S':
                            clear()
                            ligado = False
                            break
                        else:
                            contador = 0
                            continue
                
                while ligado:
                    print("\nFim de sequência. Deseja sair? S / N")
                    sn = input(">> ")

                    if sn == 'n' or sn == 'N':
                        clear()
                        break
                    elif sn =='s' or sn == 'S':
                        clear()
                        ligado = False
                        break
                    else:
                        clear()
                        print("\nInsira S ou N.")
                        
            except ValueError:
                clear()
                print("Insira um número.\n")
            
            if ligado == False:
                break
        
    elif esc == '2':
        clear()
        while True:
            print("\n+ CALCULADORA +\n\n[1] - Adição\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Tabuada\n[0] - Sair")
            calc = input(">> ")

            if calc == '1':
                clear()
                while True:
                    try:
                        prinum = float(input("Insira o primeiro número.\n>> "))
                        clear()
                        segnum = float(input("Insira o segundo número.\n>> "))
                        clear()
                        print(f"{prinum} + {segnum} = {prinum + segnum}")
                        break
                    except ValueError:
                        clear()
                        print("Insira apenas números.")
                        
            elif calc == '2':
                clear()
                while True:
                    try:
                        prinum = float(input("Insira o primeiro número.\n>> "))
                        clear()
                        segnum = float(input("Insira o segundo número.\n>> "))
                        clear()
                        print(f"{prinum} - {segnum} = {prinum - segnum}")
                        break
                    except ValueError:
                        clear()
                        print("Insira apenas números.")
                        
            elif calc == '3':
                clear()
                while True:
                    try:
                        prinum = float(input("Insira o primeiro número.\n>> "))
                        clear()
                        segnum = float(input("Insira o segundo número.\n>> "))
                        clear()
                        print(f"{prinum} x {segnum} = {prinum * segnum}")
                        break
                    except ValueError:
                        clear()
                        print("Insira apenas números.")
                        
            elif calc == '4':
                clear()
                while True:
                    try:
                        prinum = float(input("Insira o primeiro número.\n>> "))
                        clear()
                        segnum = float(input("Insira o segundo número.\n>> "))
                        clear()
                        print(f"{prinum} / {segnum} = {prinum / segnum}")
                        break
                    except ValueError:
                        clear()
                        print("Insira apenas números.")
                
            elif calc == '5':
                clear()
                ligado = True
                while ligado:
                    try:
                        tab = int(input("Insira um número entre 1 e 1000.\n>> "))
                        
                        if tab < 1 or tab > 1000:
                            clear()
                            print("O número tem que ser entre 1 e 1000.\n")
                            continue
                        
                        clear()
                        tabquant = int(input("Insira a quantidade de vezes que quer multiplicar este número.\n>> "))
                        
                        print("\n------------------\n")
                        
                        conta = 0
                        contador = 0

                        for i in range(1, tabquant + 1):
                            print(f"{tab} x {i} = {tab * i}")
                            conta += 1
                            contador += 1
                            
                            if contador == tabquant:
                                print("\nFim da tabuada.\n\nPressione no enter (ou qualquer caracter) para fazer outra. Se quiser sair, insira um 'S'.")
                                cont = input(">> ")
                                print("")
                                if cont == 's' or cont == 'S':
                                    clear()
                                    ligado = False
                                    break
                                else:
                                    continue
                            
                            if conta == 20:
                                print("\nPressione no enter (ou qualquer caracter) para continuar. Se quiser sair, insira um 'S'.")
                                cont = input(">> ")
                                print("")
                                if cont == 's' or cont == 'S':
                                    clear()
                                    ligado = False
                                    break
                                else:
                                    conta = 0
                                    continue
                            
                    except ValueError:
                        clear()
                        print("Insira um número válido.\n")
                    
                    clear()

                    if ligado == False:
                        break
            
            elif calc == '0':
                clear()
                break
            else:
                clear()
                print("Insira uma escolha válida.")
            
    elif esc == '0':
        print("\nAdeus.")
        break
    else:
        clear()
        print("Insira uma escolha válida.")