produtos = []

while True:
    produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")

    if produto.lower() == "fim":
        break

    produtos.append(produto)

nome = input("\nDigite o nome do produto que deseja procurar: ")

if nome in produtos:
    posicao = produtos.index(nome)
    print(f"O produto '{nome}' está cadastrado na posição {posicao}.")
else:
    print(f"O produto '{nome}' não está cadastrado.")
    
        
    