alunos = []
medias = []

while True:
    nome = input("Nome do aluno: ")

    notas = []
    for i in range(4):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)

    media = sum(notas) / 4

    alunos.append(nome)
    medias.append(media)

    continuar = input("Deseja cadastrar outro aluno? (s/n): ")

    if continuar.lower() != "s":
        break

print("\n=== RELATÓRIO ===")

for i in range(len(alunos)):
    if medias[i] >= 7:
        situacao = "Aprovado"
    elif medias[i] >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"Aluno: {alunos[i]}")
    print(f"Média: {medias[i]}")
    print(f"Situação: {situacao}\n")

print(f"Maior média da turma: {max(medias):.2f}")
print(f"Menor média da turma: {min(medias):.2f}")
print(f"Média geral da turma: {sum(medias) / len(medias):.2f}")
            