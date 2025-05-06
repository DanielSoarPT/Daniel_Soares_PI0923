numeros = [1, 2, 4, 8, 10]
#index     0  1  2  3  4

opc = 0
while True:
    print("[1] - Listar")
    print("[2] - Insert")
    print("[3] - Delete")
    print("[4] - Procurar")
    print("[5] - Sair")
    opc = int(input("Escolha a opc: "))

    match opc:
        case 1:
            #Listar lista
            for i in range(len(numeros)):
                print(numeros[i])
        case 2:
            #Inserir na lista
            while True:
                numeros.append(int(input("Insert Number: ")))
                stop = input("Y / Yes para parar de introduzir: ")
                if stop == 'Y' or stop == "Yes":
                    break
        case 3:
            #Delete dalista
            numeros.remove(int(input("Intrud nunmero para remover: ")))
        case 4:
            #Procurar da lista
            numcompar = int(input("Numero para procura: "))
            for i in range(len(numeros)):
                if(numeros[i] == numcompar):
                    print("Encontrei o seu numero: ", numeros[i])
        case 5:
            break
        case _:
            print("Errou a opcao")