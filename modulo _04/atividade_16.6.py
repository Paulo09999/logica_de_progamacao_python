produtos = [
    {"nome": "Arroz", "preco": 25, "estoque": 10},
    {"nome": "Feijão", "preco": 8, "estoque": 20},
    {"nome": "Macarrão", "preco": 5, "estoque": 15}
]

nome = input("Digite o nome do produto: ")

achou = False

for produto in produtos:
    if produto["nome"] == nome:
        produto["estoque"] = int(input("Nova quantidade: "))
        achou = True

if achou:
    print("Estoque atualizado!")
else:
    print("Produto não encontrado!")

print(produtos)
