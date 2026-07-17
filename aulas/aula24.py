"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamneto [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da str
"""
variavel = "olá mundo"
print(variavel[4:])
print(variavel[:5])
print(variavel[-8:-2])
print(variavel[0:len(variavel):1])
print(variavel[0:9:2])
print(variavel[-1:-10:-1])
