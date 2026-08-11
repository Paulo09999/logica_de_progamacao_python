aprovados = 0
recuperacao = 0
reprovados = 0

alunos = []

for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    media = float(input("Digite a média final: "))

    if media >= 7:
        situacao = "Aprovado"
        aprovados += 1
    elif media >= 5:
        situacao = "Recuperação"
        recuperacao += 1
    else:
        situacao = "Reprovado"
        reprovados += 1

    alunos.append({
        "nome": nome,
        "media": media,
        "situacao": situacao
    })

print("\nRELATÓRIO DOS ALUNOS")
print("-" * 40)

for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Média: {aluno['media']:.1f}")
    print(f"Situação: {aluno['situacao']}")
    print("-" * 40)

print("\nRESUMO FINAL")
print(f"Quantidade de aprovados: {aprovados}")
print(f"Quantidade de alunos em recuperação: {recuperacao}")
print(f"Quantidade de reprovados: {reprovados}")
