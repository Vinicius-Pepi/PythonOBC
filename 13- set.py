gameSet = {"Fifa 23",
           "Red Dead 2",
           "Star Wars",
           "The Legend of Zelda",
           "Mario Odyssey",
           "Resident Evil 4"}

#- Não possibilita recuperar valores via fatiamento

#1- Buscar o tamanho do set
print(len(gameSet))

#2- True e 1 são considerados o mesmo valor
exampleSet = {"Fifa 23",
              True,
              1,
              90.50}
print(exampleSet)

#3- adicionar item de outro set
gameSet.update(exampleSet)
print(gameSet)

#4- remover um item no set
gameSet.remove(True)
gameSet.remove(90.50)
print(gameSet)

