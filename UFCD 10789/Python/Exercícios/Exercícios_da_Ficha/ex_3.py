# Ler a nota de 10 alunos, calcular a media e mostrar essa média.

num = 0
media = 0
notas = []

for i in range(1, 11):
    try:
        nota = int(input("Insira uma nota de um aluno: "))
    except ValueError:
        print("\nPor favor insira uma nota valida.\n")
        continue
    
    notas.append(nota)
    num += 1

for i in notas:
    media += i

media = media / num

print(f"A media dos alunos é: {media}")