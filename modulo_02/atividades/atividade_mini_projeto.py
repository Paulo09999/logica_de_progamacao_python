#Desenvolva um programa que simule o cadastro simplificado de livros de uma biblioteca.
# O sistema deverá apresentar um menu com as seguintes opções:
# 1 - Cadastrar livro
# 2 - Listar livros
# 3 - Pesquisar livro
# 4 - Remover livro
# 5 - Encerrar
# Os livros deverão ser armazenados em uma lista durante toda a execução do programa.
# Ao pesquisar ou remover um livro inexistente, o sistema deverá informar o usuário.
livros = []

while True:
    print("\n=== BIBLIOTECA ===")

    print("1 - Cadastrar livro")

    print("2 - Listar livros")

    print("3 - Pesquisar livro")

    print("4 - Remover livro")

    print("5 - Encerrar")
    
    opcao = int(input("Escolha uma opção: "))
    
    match opcao:
        case 1:
            livro = input("Digite seu livro: ")
            livros.append(livro)
            print("Livro cadastrado")
        case 2:
            print (f"Livros cadastrados:  {livros} ")
        case 3:
            livro = input("Digite o nome do livro: ")
            if livro in livros:
                print(f"Aqui está o livro:  {livro}")
            else:
                print("Livro nao encontrado.")
        case 4:
            livro = input("Digite o livro que deseja remover: ")            
            livros.remove(livro)
            print(f"O livro: {livro} foi removido.")
                
        case 5:
            print("Progama encerrado")    
            break
            
            
            
                
            
    