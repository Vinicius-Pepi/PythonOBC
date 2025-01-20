#1- Função para imprimir hello world
def wellcome():
    print("Hello World")
    
wellcome()  

#2- Função para somar dois numeros
def sum():
    return 5 + 4

print(sum())

#3- Função para cadastrar um jogo
def create_game():
    gameName = input("Digite o nome do jogo\n")
    yearLaunch = int(input("Digite o ano de lançamento do jogo:\n"))
    gamePrice = float(input("Digite o preço do jogo:\n"))
    noteRating = float(input("Digite a nota de avaliação do jogo:\n"))
    print(f"{gameName} - R$ {gamePrice}")

create_game()   