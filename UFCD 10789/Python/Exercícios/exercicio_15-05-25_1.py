nomes = []
verd = True

while verd:
    print("\n- Menu -\n")
    print("1 - Introduzir nome")
    print("2 - Listar nomes")
    print("3 - Sair do programa")
    try:
        decs = int(input("Insira uma opção: "))
    except ValueError:
        print("\nValor incorreto, por favor insira um número.")
        continue
    
    match decs:
        case 1:
            nomes.append(input("\nIntroduza um nome: "))
            for i in nomes:
                sair = input("Deseja sair? S ou N: ")
                if sair == 'S' or sair == 's':
                    break
                nomes.append(input("\nIntroduza um nome: "))
        case 2:
            print("\n - Nomes -")
            for i in nomes:
                print(i)
        case 3:
            print("\nAté à proxima!")
            verd = False
            continue
        case default:
            print("\nInsira uma opção correta.")