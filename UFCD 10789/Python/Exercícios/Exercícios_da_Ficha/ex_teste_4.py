""" 
Criar um programa em Python para gerenciar um catálogo de até 100 livros.
O programa deve permitir que o usuário realize as seguintes operações: 
Cadastrar livros: 
O programa deve permitir que o usuário adicione novos livros ao catálogo, informando o título, o autor e o ano de publicação. 
Procurar por livros: 
O usuário deve poder procurar por título ou autor.
O programa deve exibir as posições onde o livro foi encontrado e mostrar o conteúdo correspondente. 
Excluir livros: 
O usuário deve poder excluir um livro a partir da sua posição no catálogo. A posição será dada pelo índice do livro na lista. 
Ordenar livros: 
O programa deve permitir que o usuário ordene os livros cadastrados por título ou autor. 
Listar todos os livros cadastrados: 
O programa deve listar todos os livros cadastrados, exibindo as informações de cada um (título, autor, ano). 
Sair do programa: 
O programa deve continuar em execução até que o usuário escolha explicitamente a opção de sair. 
 
Menu do Programa: 
O programa deve apresentar um menu com as seguintes opções: 
Adicionar novo livro 
Procurar por título ou autor 
Excluir livro 
Ordenar livros 
Listar livros 
Sair do Programa 
 
Requisitos: 
O programa deve permitir a execução contínua das operações, retornando sempre ao menu principal após cada ação. 
As operações de busca, exclusão e ordenação devem ser realizadas com base nas listas de títulos e autores. 
O programa deve garantir que não sejam cadastrados mais de 100 livros. 
Adicionar a possibilidade de verificar se o livro já está cadastrado antes de permitir o cadastro. 
 
8 pontos do teste estão destinados a: 
 - (2) Criar Algoritmos de procura e de validação. 
 - (2) Funções e reutilização das mesmas. 
 - (1) Utilização de boas praticas e standards. 
 - (1) Uso de Exceções. 
 """
 
import os

livs = []
cont = 0

def clear():
    os.system("cls")

def menu():
    print("+ MENU LIVRARIA +\n")
    print("[1] - Adicionar Livro")
    print("[2] - Procurar Livro por Título ou Autor")
    print("[3] - Excluir Livro")
    print("[4] - Ordenar Livros")
    print("[5] - Listar Livros")
    print("[0] - Sair")

def adicionarLivro():
    global cont
    clear()
    
    if cont == 100:
        clear()
        print("- Este catálogo já tem 100 livros. -\n")
        return
    
    while True:
        print("- Insira o nome do livro. -")
        nome = input(">> ")
        
        if not nome:
            clear()
            print("- Insira um nome! -\n")
            continue
        
        existe = False
        
        for livros in livs:
            if nome == livros['nome']:
                clear()
                print("- Este nome já existe! -\n")
                existe = True
                break
            
        if existe == True:
            continue
        
        break
    
    clear()
    while True:
        print("- Insira o autor do livro. -")
        autor = input(">> ")
        if not autor:
            clear()
            print("- Insira um autor! -\n")
            continue
        break            
    
    clear()
    while True:
        try:
            print("- Insira o ano de publicação do livro. -")
            ano = int(input(">> "))
            if not autor:
                clear()
                print("- Insira um ano! -\n")
                continue 
            break
        except ValueError:
            clear()
            print("- Insira um ano! -\n")
            continue
    
    clear() 
    livro = {
        "nome": nome,
        "autor": autor,
        "ano": ano
    }
    
    livs.append(livro)
    cont += 1
    print("- Livro adicionado ao catálogo! -\n")
    print(f"- Quantidade de livros agora no catálogo: {cont} -\n")

def procurarLivro():
    if not livs:
        clear()
        print("- Ainda não existe nenhum livro no catálogo! -\n")
        return
    
    clear()
    while True:
        print("+ MENU PROCURA +\n")
        print("[1] - Procura por Nome do Livro")
        print("[2] - Procura por Autor")
        print("[0] - Sair")
        opc = input(">> ")

        if opc == '1':
            clear()
            sair = False
            while True:
                print("- Insira o nome do livro que quer procurar. -")
                nome_proc = input(">> ")
                
                if not nome_proc:
                    clear()
                    print("- Tem que insirir o nome do livro que quer procurar. -\n")
                    continue
                
                i = 1
                for livro in livs:
                    if livro['nome'] == nome_proc:
                        clear()
                        print("- Livro encontrado! -\n")
                        print(f"+ LIVRO {i} +\n\n- Nome: {livro['nome']}\n- Autor: {livro['autor']}\n- Data: {livro['ano']}\n")
                        sair = True
                    i += 1
                
                if sair == True:
                    break
                
                clear()
                print("- Livro não encontrado! -\n")
                break
        elif opc == '2':
            clear()
            sair = False
            while True:
                print("- Insira o autor do livro que quer procurar. -")
                autor_proc = input(">> ")
                
                if not autor_proc:
                    clear()
                    print("- Tem que insirir o autor do livro que quer procurar. -\n")
                    continue
                
                clear()
                print("- Livro(s) encontrado(s)! -\n")
                achou = False
                i = 1
                for livro in livs:
                    if livro['autor'] == autor_proc:
                        print(f"+ LIVRO {i} +\n\n- Nome: {livro['nome']}\n- Autor: {livro['autor']}\n- Data: {livro['ano']}\n")
                        sair = True
                        i += 1

                if sair == True:
                    break
                
                clear()
                print("- Livro não encontrado! -\n")
                break
        elif opc == '0':
            clear()
            break
        else:
            clear()
            print("- Insira uma opção válida! -\n")
            continue

def excluirLivro():
    global cont
    if not livs:
        clear()
        print("- Ainda não existe nenhum livro no catálogo! -\n")
        return

    clear()
    while True:
        try:
            print("- Insira o número do livro que quer excluir. -\n")
            num = int(input(">> "))

            if num < 1 or num > len(livs):
                clear()
                print("- Este livro não existe! -\n")
                continue
            else:
                clear()
                livs.pop(num - 1)
                cont -= 1
                print("- Livro apagado! -\n")
                break
        except ValueError:
            clear()
            print("- Insira um número válido! -\n")
            continue

def pegarTitulo(livro):
    return livro['nome'].lower()

def pegarAutor(livro):
    return livro['autor'].lower()

def ordenarLivros():
    if not livs:
        clear()
        print("- Ainda não existe nenhum livro no catálogo! -\n")
        return
    clear()
    while True:
        print("+ MENU ORDENAR LIVROS +\n")
        print("[1] - Ordenar por Título")
        print("[2] - Ordenar por Autor")
        print("[0] - Sair")
        opc = input(">> ")

        if opc == '1':
            livs.sort(key=pegarTitulo)
            clear()
            print("- Livros ordenados por título! -\n")
            break
        elif opc == '2':
            livs.sort(key=pegarAutor)
            clear()
            print("- Livros ordenados por autor! -\n")
            break
        elif opc == '0':
            clear()
            break
        else:
            clear()
            print("- Insira uma opção válida! -\n")

def listarLivros():
    if not livs:
        clear()
        print("- Ainda não existe nenhum livro no catálogo! -\n")
        return
    
    clear()
    i = 1
    for livros in livs:
        print(f"+ LIVRO {i} +\n\n- Nome: {livros['nome']}\n- Autor: {livros['autor']}\n- Data: {livros['ano']}\n")
        i += 1
    input("- Insira qualquer tecla para sair. -\n>> ")
    clear()

def quit():
    clear()
    print("- Adeus! -\n")

def executarMenu():
    while True:
        menu()
        opc = input(">> ")
        
        if opc == '1':
            adicionarLivro()
        elif opc == '2':
            procurarLivro()
        elif opc == '3':
            excluirLivro()
        elif opc == '4':
            ordenarLivros()
        elif opc == '5':
            listarLivros()
        elif opc == '0':
            quit()
            break
        else:
            clear()
            print("- Insira uma opção válida! -\n")

clear()
executarMenu()