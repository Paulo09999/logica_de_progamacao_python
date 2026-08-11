
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
cidade = input("Digite a cidade: ")
profissao = input("Digite a profissão: ")


pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade,
    "profissao": profissao
}

print("\n Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
print("Profissão:", pessoa["profissao"])