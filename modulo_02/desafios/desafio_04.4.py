livros = []

while True:
    print("\n1-Cadastrar")
    print("2-Listar")
    print("3-Pesquisar")
    print("4-Atualizar")
    print("5-Remover")
    print("6-Sair")

    op = input("Opção: ")

    if op == "1":
        livro = {}
        livro["titulo"] = input("Título: ")
        livro["autor"] = input("Autor: ")
        livro["ano"] = input("Ano: ")
        livro["disp"] = input("Disponível (sim/não): ")

        livros.append(livro)

    elif op == "2":
        for i in livros:
            print(i)

    elif op == "3":
        titulo = input("Título: ")

        for i in livros:
            if i["titulo"] == titulo:
                print(i)
                break
        else:
            print("Livro não encontrado")

    elif op == "4":
        titulo = input("Título: ")

        for i in livros:
            if i["titulo"] == titulo:
                i["disp"] = input("Nova disponibilidade: ")
                print("Atualizado!")
                break
        else:
            print("Livro não encontrado")

    elif op == "5":
        titulo = input("Título: ")

        for i in livros:
            if i["titulo"] == titulo:
                livros.remove(i)
                print("Livro removido!")
                break
        else:
            print("Livro não encontrado")

    elif op == "6":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")