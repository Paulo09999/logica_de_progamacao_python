livro = {
    "titulo": input("Digite o título do livro: "),
    "autor": input("Digite o autor do livro: "),
    "ano": input("Digite o ano de publicação: "),
    "quantidade de paginas": input("Digite a quantidade de páginas: "),
    "disponibilidade": input("Digite a disponibilidade: ")
}

while True:
    print("\n1 - Consultar informação")
    print("2 - Alterar informação")
    print("3 - Adicionar informação")
    print("4 - Remover informação")
    print("5 - Visualizar cadastro")
    print("6 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        chave = input("Digite a informação que deseja consultar: ")
        print(livro.get(chave, "Informação não encontrada."))

    elif opcao == "2":
        chave = input("Digite a informação que deseja alterar: ")

        if chave in livro:
            livro[chave] = input("Digite o novo valor: ")
        else:
            print("Informação não encontrada.")

    elif opcao == "3":
        chave = input("Digite o nome da nova informação: ")

        if chave not in livro:
            livro[chave] = input("Digite o valor: ")
        else:
            print("Essa informação já existe.")

    elif opcao == "4":
        chave = input("Digite a informação que deseja remover: ")

        if chave in livro:
            livro.pop(chave)
            print("Informação removida.")
        else:
            print("Informação não encontrada.")

    elif opcao == "5":
        for chave, valor in livro.items():
            print(chave, ":", valor)

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")