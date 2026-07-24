#exercicio 1
"""
numero = input("Digite um número inteiro: ")

try:
    numero_int = int(numero)
except:
    print("Você não digitou um número inteiro")

if numero_int % 2 == 0:
    print(f"O número {numero_int} é par ")
else:
    print(f"O número {numero_int} é ímpar ")

"""

# exercicio 2
"""
horario = input("Digite o horario atual no sistema militar:")

try:
    horario_int = int(horario)

    if horario_int < 6:
        print(f"Boa Madrugada: {horario_int}")
    elif 6 <= horario_int < 12:
        print(f"Bom dia: {horario_int}")
    elif 12 <= horario_int  < 18:
        print(f"Boa Tarde: {horario_int}")
    elif 18 <= horario_int <= 23:
        print(f"Boa noite: {horario_int}")
    else:
        print("Você não digitou um horário valido")
except:
    print("Digite um numero inteiro")
"""


nome_primeiro = input("Digite seu primeiro nome: ")
nome_primeiro_contar = len(nome_primeiro)
#print(nome_primeiro_contar)

if 1 <= nome_primeiro_contar <= 4:
    print(f"Seu nome é curto: {nome_primeiro}")
elif 5 <= nome_primeiro_contar <= 6:
    print(f"Seu nome é normal: {nome_primeiro}")
elif nome_primeiro_contar > 6:
    print(f"Seu nome é muito grande: {nome_primeiro}")
else:
    print("Digite um nome valido")