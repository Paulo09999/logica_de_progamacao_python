nome_do_produto = input("digite o nome do produto: ")
preço_unitário = float(input("digite o nome do preço unitario: R$"))
quantidade = int(input("digite a quantidade: "))
percentual_de_desconto = float(input("digite o percentual de desconto (%) : "))

subtotal = preço_unitário * quantidade
valor_desconto = subtotal * percentual_de_desconto / 100
total = subtotal - valor_desconto

print(subtotal)
print(valor_desconto)
print(total)
print("se o total é maior que R$ 100,00" is True)
print("se o nome do produto contém a letra a" is True)
print("se o desconto é diferente de None" is False)

