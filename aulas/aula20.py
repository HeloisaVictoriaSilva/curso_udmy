# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
senha = input("Senha: ")

# if senha == "123456":
#     print("Entrou")
# else:
#     print("senha incorreta.")
if not senha:
    print("senha incorreta.")

print(not True)
print(not False)