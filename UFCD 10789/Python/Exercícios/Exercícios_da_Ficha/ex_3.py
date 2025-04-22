# Ler a nota de 10 alunos, calcular a media e mostrar essa média.

num = 0
media = 0
notas = []

while num != 10:
    try:
        nota = int(input("Insira uma nota de um aluno: "))
    except ValueError:
        print("\nPor favor insira uma nota valida.\n")
        continue
    
    notas.append(nota)
    num += 1
    
num = 0

for i in notas:
    media += i
    num += 1

media = media / num

print(f"A media dos alunos é: {media}")