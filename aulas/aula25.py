"""
Introdução ao try/except
try -> tentar exexcutar o código
except -> ocorreu
"""
numero = input("Vou dobrar o número que você digitar: ")

try:
    numero_float = float(numero)
    print(f"O dobro de {numero} é {numero_float * 2}")
except:
    print("Isso não é um número")

#print(numero.isdigit())

# if numero.isdigit():
#     numero_float = float(numero)
#     print(f"O dobro de {numero} é {numero_float * 2}")
# else:
#     print("Isso não é um número")