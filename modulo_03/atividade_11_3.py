nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
cidade = input("Digite sua cidade: ")

pessoa = {
    "nome": nome,
    "email": email,
    "cidade": cidade
}

consulta = input("Digite a categoria: ")

valors = pessoa.get(consulta)

if valors is not None:
    print("\n Valor encontrado:", valors)
else:
    print("\nDado não encontrado.")



