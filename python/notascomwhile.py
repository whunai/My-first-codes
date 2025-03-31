notas = []
contador = 1

while contador <= 5:
    nomeAluno = input("Nome do aluno: ")
    nota = float(input("Nota: "))
    resultado = [nomeAluno, nota]
    notas.append(resultado)
    contador += 1