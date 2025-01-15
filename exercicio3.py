'''
Exercicio 3:

* Cálculo de distância:
-> Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km, e R$0,35 para viagens mais longas

'''


distancia = float(input("Escreva a distância da viagem:\n"))

if distancia <= 200:
    preco = distancia * 0.50

else:
    preco = distancia * 0.35
print(f"O preço da sua viagem é\nR$: {preco:.2f}")


'''

* Aumento salário funcionário
-> Escreva um programa que pergunte o salário do funcionário e 
calcule o valor do aumento. Para salários superiores a R$ 1.250,00 calcule um aumento de 10%.
Para os inferiores ou iguals, de 15%

'''

salario = float(input("Escreva o seu salário: "))

if salario > 1250:  
    reajuste = (salario * 0.10) + salario
    print(f"Seu salário novo é de:\nR$ {reajuste}")
else:
    reajuste = (salario * 0.15) + salario
    print(f"Seu salário novo é de:\nR$ {reajuste}")