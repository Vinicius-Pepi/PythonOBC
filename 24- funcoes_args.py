"""
*args  
- Utilizamos ele quando nao temos certeza de quantos argumentos queremos ter numa função
- Os argumentos são passados como uma tupla

**kwargs - Além dos valores podemos passar também as respectivas chaves para cada argumento
- Os argumentos são passados como um dicionário
"""

#1- Soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")
    
#2- Apresentação de cursos
def presentation(**data):
    for key, value in data.itens():
        print(f"{key} - {value}")
        
presentation(name="Python", category="Backend", level="Iniciante")