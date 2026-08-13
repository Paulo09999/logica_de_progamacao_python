contatos =[]
item = {}



for i in range(3):
    item ["nome"] = input ("Digite o nome: ")
    item ["Telefone"] = input ("Digite o numero de telefone: ") 
    item ["e-mail"] = input ("Digite seu e-mail: ")




categoria = input ("Digite os dados: ")
contatos.append(item.copy())
item.clear()
    
for i in contatos:
    if i["nome"] == categoria:
        print("\n encontrado")
        break
    
    else:
        print("\n nao encontrado")