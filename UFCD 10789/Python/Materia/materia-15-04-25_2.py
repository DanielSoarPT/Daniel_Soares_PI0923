noms = ['Daniel', 'Ricardo', 'Ivan', 'João']

while True:
    dec = input("Deseja continuar? S ou N:  ")
    if dec == "N" or dec == "n":
        break
    noms.append(input("Introduza um novo nome: "))