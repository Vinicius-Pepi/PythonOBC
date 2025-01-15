import time
import platform
'''
Exercício 4
* Contagem regressiva:
-> Faça um programa para escrever a contagem regressiva do lançamento de um foguete. 
O programa deve imprimir 10,9,8,...,1,0 e disparar um "beep"
'''
i = 10
while(i >= 0):
    print(i)
    i -= 1
    time.sleep(1)
print("Foguete lançado!")

if platform.system() == "Windows":
    import winsound
    winsound.Beep(1000, 500)
else:
    import pygame
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Beep/beep.wav") 
    sound.play()   
   
'''
*Tabuada:
-> Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
'''

num1 = int(input("Digite o número para calcular a tabuada: "))
init = int(input("Até qual valor você quer iniciar a tabuada? "))
final = int(input("Até qual valor você quer finalizar a tabuada? "))

i = init

while(i <= final):
    resultado = num1 * i
    print(f"{num1} x {i} = {resultado}")
    i += 1