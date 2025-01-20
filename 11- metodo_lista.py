gamesList = ["Resident Evil 4", 
             "Star Wars Jedi Survivor", 
             "The legend of Zelda", 
             "Red Dead 2"]

#1- Tamanho da lista
print(len(gamesList))   

#2- Recuperar um item da lista pelo índice
print(gamesList.index("Star Wars Jedi Survivor"))

#3- Adicionar item ao final da lista
gamesList.append("Gta V")
print(gamesList)

#4- Ordenar lista
gamesList.sort()
print(gamesList)

#5- Copiar os itens de uma lista para outra
gameReset = gamesList.copy()
gameReset.remove("Red Dead 2")
print(gameReset)

#6- Remove todos os itens da lista
gamesList.clear()
print(gamesList)