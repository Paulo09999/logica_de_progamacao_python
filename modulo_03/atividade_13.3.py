funcionario = {
    "nome": input("Nome: "),
    "cargo": input("Cargo: "),
    "setor": input("Setor: "),
    "salario": input("Salário: ")
}

chave = input("Chave para remover: ")

if chave in funcionario:
    del funcionario[chave]
else:
    print("Chave não existe.")

print(funcionario)