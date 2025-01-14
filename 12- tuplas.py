gamesTuple = ("Fifa 23",
              "Red Dead 2",
              "Mario Odyssey",
              "The Legend of Zelda")

print(gamesTuple)
print(type(gamesTuple))

# - Não possibilita adicionar valores na tupla
# - Não possibilita remover valores na tupla
# - Não possibilita ordenar valores na tupla

#1- Buscar os dois primeiros itens da tupla
print(gamesTuple[0:2])

#2- Buscar o ultimo item da lista
print(gamesTuple[-1])

#3- Buscar jogos até uma determinada posição
print(gamesTuple[:3])

#4- Buscar jogos de uma posição em diante
print(gamesTuple[2:])

#5- recuperar um item da tupla pelo indice
print(gamesTuple.index("Red Dead 2"))