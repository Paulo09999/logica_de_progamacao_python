nome = input("Digite o nome do produto: ")
preco = int(input("Digite o  preço: "))
estoque = int(input("Digite a quantidade de estoque: "))




produtos = {
    "nome" : nome,
    "preco" : preco,
    "estoque" : estoque
}
print("\nPRODUTOS ARMAZENADOS")
produtos["categoria"] = "periferiocos"
produtos["estoque"] = estoque
produtos["estoque"] += 3

for chave, valor in produtos.items():
    print(chave, valor)