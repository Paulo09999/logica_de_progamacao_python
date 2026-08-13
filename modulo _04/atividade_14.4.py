
produtos = []
item = {}

for i in range(5):

    item["nome"] = input("Digite o nome do produto: ")
    item["categoria"] = input("Digite a categoria do produto: ")
    item["preco"] = input("Digite o preço do produto: ")
    item["quantidade"] = input("Digite a quantidade em estoque: ")

    produtos.append(item.copy())
    item.clear()

for chave in produtos:
    print(chave)

    
 

    