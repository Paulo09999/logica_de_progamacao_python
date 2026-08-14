aluno =[]
item = {}



for i in range(3):
    item ["nome"] = input ("Digite o nome do aluno : ")
    item ["nome"] = input ("Digite o nome do aluno : ") 
    item ["nome"] = input ("Digite o nome do aluno: ")


aluno.append(item.copy())   


categoria = input ("Digite o nome que deseja remover: ")


for i in aluno:
    if i["nome"] == categoria:
        resposta = input("deseja remover esete aluno? (s\n)")
        
        
        aluno.remove(i)  
        if resposta.lower() == "s":
            print("Aluno removido")
            break
else:
    print("Aluno nao encontrado ")      
    for i in aluno:
        print(i)
          