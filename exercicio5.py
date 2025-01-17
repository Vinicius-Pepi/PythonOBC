"""
Exercicio 5:
*Conta letras maiúsculas e minúsculas:
-> Escreva uma função Python que receba um string e conte o número de letras maiúsculas e minúsculas destra string
"""


def lowerOrUpper(): #Definindo a função
    phrase = input("Digite uma frase: ")
    upper = 0
    lower = 0
    
    for char in phrase: #Armazenando os caracteres da string phrase enquanto o loop percorre a string
        if char.isupper(): #Verificando letras maiúsculas
            upper += 1
        elif char.islower(): #Verificando letras minúsculas
            lower += 1
    print(f"Letras maiusculas: {upper}\nLetras minusculas: {lower}")
lowerOrUpper()
    
"""
*Lista de números pares e ímpares de uma lista
-> Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma
"""

evenList = []
oddList = []

def evenOrOdd():    #Definindo a função
    while True: #O Loop continua até encontrar o "break"
        try: #Uso do try para verificar se o usuário usará o input corretamente
            num = int(input("Digite um número: "))
            if num % 2 == 0: #Verificando se o número é par
                evenList.append(num) #Adicionando a variável num na lista par
                print(f"O número {num} é par")
            else:
                oddList.append(num) #Adicionando a variável num na lista ímpar
                print(f"O número {num} é ímpar")
        except ValueError: #Caso o usuário use o input incorretamente
            print("Valor inválido, tente novamente")
            continue
            
        choice = input("Deseja adicionar mais um número? (s/n)").lower()
        if choice != "s":
            break #Fim da repetição
        
evenOrOdd()
print(f"Lista de números pares:\n{evenList}")
print(f"Lista de números ímpares:\n{oddList}")
