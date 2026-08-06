notas = []


for i in range(10):
    nota = float(input(f"Digite a nota do {i+1}º estudante: "))
    notas.append(nota)
    
print("\nNotas em ordem crescente:")
print(sorted(notas))


print("\nNotas em ordem decrescente:")
print(sorted(notas, reverse=True))


print("\nMaior nota:", max(notas))


print("Menor nota:", min(notas))


media = sum(notas) / len(notas)
print("Média da turma:", media)