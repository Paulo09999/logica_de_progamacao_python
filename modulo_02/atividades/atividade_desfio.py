quantidade = 0
total = 0

maior = 0
menor = 0

while True:
    venda = float(input("Digite o valor da venda (0 para sair): "))

    if venda == 0:
        break

    quantidade += 1
    total += venda

    if quantidade == 1:
        maior = venda
        menor = venda
    else:
        if venda > maior:
            maior = venda

        if venda < menor:
            menor = venda

media = total / quantidade

print("Quantidade de vendas:", quantidade)
print("Total vendido:", total)
print("Média das vendas:", media)
print("Maior venda:", maior)
print("Menor venda:", menor)