produtos = []
 
for i in range(5):
    nome = input(f"Digite o nome do{i+1}º produto: ")
    quantidade = int(input("Digite a quantidade de estoque: "))
    
    produtos.append({
        "nome": nome,
        "quantidade" : quantidade
    })
    
print("\nProdutos com quantidade igual ou inferior a 5 unidades: ")    
encontrado =  False
for produto in produtos:
    if produtos["quantidade"] <= 5 :
        print(f"-{produto['nome']} ({produto['quantidade']} unidades)")
        encontrado = True
        if not encontrado:
            print ("Nenhum produto possui quantidade igual ou inferior a 5 unidades.")
    