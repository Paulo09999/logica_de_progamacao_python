idade = 18 
possui_cracha = True
esta_bloqueado = False

# pode_entrar = idade >= 18 and possui_cracha
# esta_bloqueado = idade < 18 or not possui_cracha
# esta_bloqueado = idade >= 18 and not possui_cracha

# print(pode_entrar)
# print(esta_bloqueado)
# print(esta_bloqueado)



print(idade >= 18 and possui_cracha) #True
print(idade < 18 or possui_cracha) #false
print(not esta_bloqueado) #True
print(idade >= 18 and not esta_bloqueado) #True
print(possui_cracha and esta_bloqueado) #False
