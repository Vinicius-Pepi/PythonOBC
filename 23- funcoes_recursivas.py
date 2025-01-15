#1- Fatorial de um numero
def factorial(num):
    if num == 1:
        return 1
    else:
        return(num * factorial(num -1))

number = int(input("Digite um número para fatorial:\n"))
print(f"O fatorial de {number} é: {factorial(number)}")

#2- Soma total de um número
def total_sum(num):
    if num == 1:
        return 1
    else:
        return(num + total_sum(num -1))
    
num = int(input("Digite um número para soma:\n"))
print(f"A soma total do {num} é: {total_sum(num)}")