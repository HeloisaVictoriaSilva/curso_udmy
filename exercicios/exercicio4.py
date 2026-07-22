nome_usuario = input("Digite seu nome: ")
idade_usuario = input("Digite sua idade em números: ")

if nome_usuario  and idade_usuario:
    print(f"Seu nome é {nome_usuario}")
    print(f"Seu nome invertido é {nome_usuario[::-1]}")
    if " " in nome_usuario:
        print(f"Seu nome conmtém espaços")
    else:
        print("Seu nome NÃO contém espaços")
    print(f"Seu nome tem {len(nome_usuario)} letras")
    print(f"A primeira letra do seu nome é {nome_usuario[0]}")
    print(f"A ultima letra do seu nome é {nome_usuario[-1]}")
else:
    print("Desculpa, você deixou campos vazios")