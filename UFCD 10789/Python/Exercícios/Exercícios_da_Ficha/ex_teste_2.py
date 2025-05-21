import os

numCli = 1  # Variável global que começa com 1
clientes = []

def clear():
    os.system("cls")

def contarDesconto(compra):
    if 100 > compra:
        return compra * 1
    if 100 <= compra <= 200:
        return compra * 0.05
    if 200 < compra < 500:
        return compra * 0.1
    if 500 <= compra:
        return compra * 0.15

def criarCliente():
    clear()
    while True:
        print("Insira o nome do cliente.")
        nome = input(">> ")
        if not nome:
            print("\n- Insira um nome! -\n")
            continue
        else:
            break
    
    while True:
        print("\nInsira a morada do cliente.")
        morada = input(">> ")
        if not morada:
            print("\n- Insira uma morada! -")
            continue
        else:
            break
    
    while True:
        try:
            print("\nInsira o número de telefone do cliente.")
            tel = int(input(">> "))
            break
        except ValueError:
            print("\n- Insira apenas digitos! -")
            continue
    
    while True:
        try:
            print("\nInsira o NIF do cliente. (9 digitos)")
            nif = int(input(">> "))
            if 100000000 <= nif <= 999999999:
                break
            else:
                print("\n- O NIF tem que ser 9 digitos! -")
                continue
        except ValueError:
            print("\n- Insira apenas digitos! -")
            continue
        
    while True:
        try:
            print("\nInsira o valor da compra do cliente.")
            compra = float(input(">> "))
            break
        except ValueError:
            print("\n- Insira apenas digitos! -")
            continue
        
    valDesconto = contarDesconto(compra)
    valFinal = compra - valDesconto
    
    cliente = {
        "numCli": numCli,
        "nome": nome,
        "morada": morada,
        "tel": tel,
        "nif": nif,
        "compra": compra,
        "valDesconto": valDesconto,
        "valFinal": valFinal,
    }
    
    clear()
    clientes.append(cliente)
    print(f"- Cliente {nome} adicionado com sucesso com o numero {numCli}! -")

def listarClientes():
    if not clientes:
        clear()
        print("- Ainda não existem clientes! -")
        
    index = 0
    clear()
    
    while True:
        cliente = clientes[index]
        print("+ Lista de Clientes +")
        print(f"\n+ Número - {cliente['numCli']}")
        print(f"+ Nome - {cliente['nome']}")
        print(f"+ Morada - {cliente['morada']}")
        print(f"+ Telefone - {cliente['tel']}")
        print(f"+ NIF - {cliente['nif']}")
        print(f"+ Compra - {cliente['compra']:.2f}€")
        print(f"+ Desconto - {cliente['valDesconto']:.2f}€")
        print(f"+ Valor Final - {cliente['valFinal']:.2f}€")
        print("\n'a' - Cliente Anterior\n'd' - Próximo Cliente\n'(Qualquer outra coisa)' - Sair")
        esc = input(">> ")
        
        if esc.lower() == 'a':
            clear()
            index -= 1
        elif esc.lower() == 'd':
            clear()
            index += 1
        else:
            clear()
            break
            
        if index < 0:
            clear()
            print("- Não existem clientes anteriores a partir daqui! -\n")
            index = 0
        elif index >= len(clientes):
            clear()
            print("- Não existem mais clientes a partir daqui! -\n")
            index = len(clientes) - 1

def procurarCliente():
    
    if not clientes:
        clear()
        print("- Ainda não existem clientes! -")
    
    clear()
    while True:
        try:
            print("Insira o numero do cliente que quer procurar.")
            num = int(input(">> "))
            
            if num < 1 or num > len(clientes):
                clear()
                print("- Este número de cliente não está na lista! -\n")
                continue
            
            cliente = clientes[num - 1]
            print(f"\n+ Número - {cliente['numCli']}")
            print(f"+ Nome - {cliente['nome']}")
            print(f"+ Morada - {cliente['morada']}")
            print(f"+ Telefone - {cliente['tel']}")
            print(f"+ NIF - {cliente['nif']}")
            print(f"+ Compra - {cliente['compra']:.2f}€")
            print(f"+ Desconto - {cliente['valDesconto']:.2f}€")
            print(f"+ Valor Final - {cliente['valFinal']:.2f}€")
            print("\n's' - Inserir outro número\n'(Qualquer outra coisa)' - Sair")
            esc = input(">> ")
        
            if esc.lower() == 's':
                clear()
                continue
            else:
                clear()
                break  
        except ValueError:
            clear()
            print("- Insira um digito válido! -\n")
            continue
        
def sair():
    clear()
    print("- Adeus! -")

while True:
    print("\n+ MENU +\n\n[1] - Inserir Novo Cliente\n[2] - Lista de Clientes\n[3] - Procurar Cliente por Numero\n[0] - Sair")
    esc = input(">> ")
    
    if esc == '1':
        criarCliente()
        numCli += 1
    elif esc == '2':
        listarClientes()
    elif esc == '3':
        procurarCliente()
    elif esc == '0':
        sair()
        break
    else:
        clear()
        print("- Escolha uma opção válida! -")