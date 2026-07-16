# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6
# H e l o i s a
#-7-6-5-4-3-2-1
nome = "Heloisa"
# print(nome[2])
# print(nome[-5])
# print("s" in nome)
# print("loi" not in nome)

nome_usuario = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")