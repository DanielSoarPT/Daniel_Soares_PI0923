# Elabore uma base de dados de clientes de uma fábrica de materiais.
# O programa deverá possibilitar inserção e listagem dos clientes bem como as compras por
# eles efetuadas( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ).
# Divida final=compra – desconto, valor do desconto se compra for entre 100 e 200 é 5%,
# se for superior a 200 e inferior a 500 é 10% se superior a 500 é 15%.
# O programa deve validar todas as entradas e na listagem deve parar cliente a cliente e ser
# possível busca direta por número de cliente. 5v. O programa deve conter (Estruturas 3v, funções .5v, Vetores .4v, apontadores .3v). 2 H

import os

def clear():
    os.system("cls")
    
def contarDesconto(compra):
    if 100 <= compra <= 200:
        return compra * 0.05
    if 200 < compra < 500:
        return compra * 0.1
    if 500 <= compra:
        return compra * 0.15
    
numCli = 1
clientes = []

while True:
    print("\n+ MENU +\n\n[1] - Inserir Novo Cliente\n[2] - Lista de Clientes\n[3] - Procurar Cliente por Numero\n[0] - Sair")
    esc = input(">> ")
    
    if esc == '1':
        clear()
        print("Insira o nome do cliente.")
        nome = input(">> ")
        
        print("\nInsira a morada do cliente.")
        morada = input(">> ")
        
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
        numCli += 1
        
    elif esc == '2':
        
        if not clientes:
            clear()
            print("- Ainda não existem clientes! -")
            continue
        
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
            
    elif esc == '3':
        
        if not clientes:
            clear()
            print("- Ainda não existem clientes! -")
            continue
        
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
            
    elif esc == '0':
        clear()
        print("- Adeus! -")
        break
    else:
        clear()
        print("- Escolha uma opção válida! -")