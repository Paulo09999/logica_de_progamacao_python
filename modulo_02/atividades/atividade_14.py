produtos = []

for i in range(10):
    produto = input(f"Digite o nome do {i+1}º produto: ")
    produtos.append(produto)

produtos.sort()

print("\nProdutos em ordem alfabética:")
for produto in produtos:
    print(produto)