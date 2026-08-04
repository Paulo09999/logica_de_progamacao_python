alunos = []

for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    alunos.append(nome)

print("\nAlunos cadastrados:")
for aluno in alunos:
    print(aluno)