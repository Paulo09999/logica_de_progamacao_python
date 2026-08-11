
alunos = []

while True:
    print("\n=== Cadastro de Aluno ===")

    nome = input("Nome do aluno: ")

    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    nota3 = float(input("Digite a 3ª nota: "))

    media = (nota1 + nota2 + nota3) / 3

    
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    
    aluno = {
        "nome": nome,
        "notas": [nota1, nota2, nota3],
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)

    continuar = input("\nDeseja cadastrar outro aluno? (S/N): ").upper()

    if continuar != "S":
        break


print("\n" + "=" * 50)
print("RELATÓRIO FINAL")
print("=" * 50)

medias = []
aprovados = 0

for aluno in alunos:
    print(f"\nAluno: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")

    medias.append(aluno['media'])

    if aluno['situacao'] == "Aprovado":
        aprovados += 1


total_alunos = len(alunos)
media_geral = sum(medias) / total_alunos
maior_media = max(medias)
menor_media = min(medias)
percentual_aprovados = (aprovados / total_alunos) * 100

print("\n" + "=" * 50)
print("ESTATÍSTICAS DA TURMA")
print("=" * 50)

print(f"Quantidade total de alunos: {total_alunos}")
print(f"Média geral da turma: {media_geral:.2f}")
print(f"Maior média: {maior_media:.2f}")
print(f"Menor média: {menor_media:.2f}")
print(f"Percentual de alunos aprovados: {percentual_aprovados:.2f}%")