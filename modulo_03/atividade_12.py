alunos = ["Ana", "Carlos", "Maria", "Pedro", "Lucas"]

nome = input("Digite um nome: ")

if nome in alunos:
    print(f"{nome} está na lista.")
    print(f"Posição: {alunos.index(nome)}")
else:
    print(f"{nome} não está na lista.")