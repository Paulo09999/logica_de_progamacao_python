notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

print("\nNotas:", notas)
print("Maior nota:", max(notas))
print("Menor nota:", min(notas))
print("Média da turma:", sum(notas) / len(notas))