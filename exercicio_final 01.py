teams = {}

def indice():
    while True:
        print("=" * 30)
        print("1- Adicionar times\n2- Excluir time\n3- Listar times\n4- Adicionar jogadores\n5- Remover jogadores\n6- Sair")
        print("=" * 30)
        try:
            choice = int(input("Escolha uma opção: "))
            if choice == 1:
                cadTeam()
            elif choice == 2:
                remTeam()
            elif choice == 3:
                listTeam()
            elif choice == 4:
                cadPlayer()
            elif choice == 5:
                remPlayer()
            elif choice == 6:
                break
            else:
                print("Digite uma opção válida")
                continue
        except ValueError:
            print("Digite apenas o número da opção desejada")   
                     
            
            
def cadTeam():
    teamName = input("Digite o nome do time que quer adicionar:\n")
    if teamName in teams:
        print("O time já está cadastrado")
    else:
        teams[teamName] = []
        
        
        
        
def remTeam():
    teamName = input("Digite o nome do time que quer remover:\n")
    if teamName in teams:
        teams.pop(teamName)
    else:
        print("O time não está cadastrado")
    
        
        
        
def listTeam():
    print(f"Lista de times cadastrados:\n{teams}")
    
    
    
def cadPlayer():
    print(teams)
    teamName = input("Digite o nome do time que deseja adicionar o jogador: ")
    if teamName in teams:
        playerName = input("Digite o nome do jogador: ")
        if playerName in teams[teamName]:
            print(f"O jogador {playerName} já está cadastrado no time {teamName}")
        else:
            teams[teamName].append(playerName)
    else:
        print(f"O time {teamName} não está cadastrado.")
        
        
        
        
def remPlayer():
    print(teams)
    teamName = input("Digite o nome do time que deseja remover um jogador: ")
    if teamName in teams:
        playerName = input("Deseja o nome do jogador que deseja remover: ")
        if playerName in teams[teamName]:
            teams[teamName].remove(playerName)
            print(f"O jogador {playerName} foi removido do time {teamName}")
        else:
            print(f"O jogador {playerName} não foi encontrado no time {teamName}")
    else:
        print(f"O time {teamName} não está cadastrado")
        
        
        
    
indice()