gameFifa = {
    "name": "Fifa 23",
    "yearLaunch": 2022,
    "gamePrice": 90.50,
    "classification": 8.5,
    "genre": ["esporte", "família"]
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

#1-  recuperar um elemento do dicionario
print(gameFifa["genre"])
print(gameFifa.get("classification"))

#2-  Buscar apenas as chaves do dicionario
print(gameFifa.keys())

#3- Buscar apenas os valores do dicionario
print(gameFifa.values())

#4- Buscar itens do dicionario com chave e valor
print(gameFifa.items())

#5- adicionar itens no dicionario
gameFifa["players"] = 2
print(gameFifa)

#5- atualizar itens no dicionario
gameFifa.update({"players": 1})
print(gameFifa)

#6- remover itens no dicionario
gameFifa.pop("players")
print(gameFifa)