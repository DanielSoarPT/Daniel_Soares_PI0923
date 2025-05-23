clinames=[]

while True:
    print("1 - Inserir nome cliente")
    print("2 - Listar Clientes")
    print("3 - Sair da app")
    opc = input(">> ")
    
    match opc:
        case "1":
            clinames.append(input("Insert nome cli"))
        case "2":
            for name in clinames:
                print("nome cli: ", name)
        case "3":
            print("Adius muxaxus")
            break
        case _:
            print("Opção não existe")