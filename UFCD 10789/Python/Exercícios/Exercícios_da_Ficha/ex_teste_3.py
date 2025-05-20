# Crie um programa para gerenciar os fornecedores de uma empresa de construção. O programa deve permitir:
# Funcionalidades:
#     Inserir os dados dos fornecedores com os seguintes campos:
#         NumFor (gerado automaticamente);
#         NomeFor (nome do fornecedor);
#         Endereço;
#         Telefone (validar se tem ao menos 9 dígitos);
#         NIF (validar se tem exatamente 9 dígitos);
#         ValorFornecido (valor total dos equipamentos fornecidos);
#         Desconto (calculado automaticamente);
#         ValorFinal = ValorFornecido - Desconto.
#         Regras de desconto:
#             Se o valor fornecido for entre 1.000 e 5.000 €, aplicar 8% de desconto;
#             Se entre 5.001 e 10.000 €, aplicar 12%;
#             Se superior a 10.000 €, aplicar 18%.
#     Listar os fornecedores um por um (parando entre cada um com um Enter);
#     Permitir busca direta por número do fornecedor (NumFor).
 
# Observações:
#     Todas as entradas devem ser validadas.
#     O programa deve ser estruturado com funções.
#     Use uma lista para armazenar os dados dos fornecedores.

import os

def clear():
    os.system("cls")
    
def contarDesconto(compra):
    if 1000 <= compra <= 5000:
        return compra * 0.08
    if 5001 <= compra <= 10000:
        return compra * 0.12
    if 10000 < compra:
        return compra * 0.18
    
numFor = 1
fornecedores = []

while True:
    print("\n+ MENU +\n\n[1] - Inserir Novo Fornecedor\n[2] - Lista de Fornecedores\n[3] - Procurar Fornecedor por Numero\n[0] - Sair")
    esc = input(">> ")
    
    if esc == '1':
        clear()
        print("Insira o nome do fornecedor.")
        nome = input(">> ")
        
        print("\nInsira a morada do fornecedor.")
        morada = input(">> ")
        
        while True:
            try:
                print("\nInsira o número de telefone do fornecedor.")
                tel = int(input(">> "))
                if 100000000 <= tel <= 999999999:
                    break
                else:
                    print("\n- O telefone tem que ter 9 digitos! -")
                    continue
            except ValueError:
                print("\n- Insira apenas digitos! -")
                continue
        
        while True:
            try:
                print("\nInsira o NIF do fornecedor. (9 digitos)")
                nif = int(input(">> "))
                if 100000000 <= nif <= 999999999:
                    break
                else:
                    print("\n- O NIF tem que ter 9 digitos! -")
                    continue
            except ValueError:
                print("\n- Insira apenas digitos! -")
                continue
            
        while True:
            try:
                print("\nInsira o valor da compra do fornecedor.")
                compra = float(input(">> "))
                break
            except ValueError:
                print("\n- Insira apenas digitos! -")
                continue
            
        valDesconto = contarDesconto(compra)
        valFinal = compra - valDesconto
        
        cliente = {
            "numFor": numFor,
            "nome": nome,
            "morada": morada,
            "tel": tel,
            "nif": nif,
            "compra": compra,
            "valDesconto": valDesconto,
            "valFinal": valFinal,
        }
        
        clear()
        fornecedores.append(cliente)
        print(f"- Cliente {nome} adicionado com sucesso com o numero {numFor}! -")
        numFor += 1
        
    elif esc == '2':

        if not fornecedores:
            clear()
            print("- Ainda não existem fornecedores! -")
            continue
        
        index = 0
        clear()
        
        while True:
            fornecedor = fornecedores[index]
            print("+ Lista de Fornecedores +")
            print(f"\n+ Número - {fornecedor['numFor']}")
            print(f"+ Nome - {fornecedor['nome']}")
            print(f"+ Morada - {fornecedor['morada']}")
            print(f"+ Telefone - {fornecedor['tel']}")
            print(f"+ NIF - {fornecedor['nif']}")
            print(f"+ Compra - {fornecedor['compra']:.2f}€")
            print(f"+ Desconto - {fornecedor['valDesconto']:.2f}€")
            print(f"+ Valor Final - {fornecedor['valFinal']:.2f}€")
            print("\n'a' - Fornecedor Anterior\n'd' - Próximo Fornecedor\n'(Qualquer outra coisa)' - Sair")
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
                print("- Não existem fornecedores anteriores a partir daqui! -\n")
                index = 0
            elif index >= len(fornecedores):
                clear()
                print("- Não existem mais fornecedores a partir daqui! -\n")
                index = len(fornecedores) - 1
            
    elif esc == '3':
        
        if not fornecedores:
            clear()
            print("- Ainda não existem fornecedores! -")
            continue
        
        clear()
        while True:
            try:
                print("Insira o numero do fornecedor que quer procurar.")
                num = int(input(">> "))
                
                if num < 1 or num > len(fornecedores):
                    clear()
                    print("- Este número de fornecedor não está na lista! -\n")
                    continue
                
                fornecedor = fornecedores[num - 1]
                print(f"\n+ Número - {fornecedor['numFor']}")
                print(f"+ Nome - {fornecedor['nome']}")
                print(f"+ Morada - {fornecedor['morada']}")
                print(f"+ Telefone - {fornecedor['tel']}")
                print(f"+ NIF - {fornecedor['nif']}")
                print(f"+ Compra - {fornecedor['compra']:.2f}€")
                print(f"+ Desconto - {fornecedor['valDesconto']:.2f}€")
                print(f"+ Valor Final - {fornecedor['valFinal']:.2f}€")
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