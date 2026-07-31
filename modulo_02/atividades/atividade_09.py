usuario = "admin"
senha = "python123"

while True:
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if usuario == "admin" and senha == "python123":
        print("Login realizado")
        break

    print("Usuário ou senha inválidos")

    
