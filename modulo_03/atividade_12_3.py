titulo = input("Digite o titulo do livro: ")
autor =  input("Digite o nome do autor: ")
ano = input("Digite o ano do livro:")
categoria = input("Digite a categoria o livro: ")


livro  = {
    "titulo": titulo,
    "autor" : autor,
    "categoria" : categoria,
    "ano": ano
}

for chave in livro.keys():
    print(chave)
    
for valor in livro.values():
    print(valor)
    
for chave in valor.items():
    print(chave, valor)
    
for chave, valor in livro.itemsa():
    print(f"{chave}: {valor}")
            