"""
Exercicio 5:
*Conta letras maiúsculas e minúsculas:
-> Escreva uma função Python que receba um string e conte o número de letras maiúsculas e minúsculas destra string
"""

"""
*Lista de números pares e ímpares de uma lista
-> Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma
"""
pairList = []
oddList = []
def pair(num):
    if num % 2 == 0:
        print(f"O número {num} é par\n")
        pairList.append(num)
    else:
        print(f"O número {num} é ímpar\n")
        oddList.append(num)
    choice = input("Deseja incluir outro número? (y/n)\n")
    if choice == "y":
        num = int(input("Escreva um número: "))
        pair(num)

num = int(input("Escreva um número: "))
pair(num)

print(f"Lista de números pares:\n{pairList}\nLista de números ímpares\n{oddList}")

