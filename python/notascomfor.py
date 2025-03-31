notas = []

for x in range(2):
    nomeAluno = input("Nome: ")
    nota = float(input("Nota: "))
    resultado = [nomeAluno, nota]
    notas.append(resultado)

print("Quantidade de notas", len(notas))

for n in notas:
    nomeAluno = n[0]
    nota = n[1]
    print("O aluno", nomeAluno, "tirou a nota:", nota)