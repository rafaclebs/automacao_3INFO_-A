'''
As funções permite modularizar o código, dividir ele em partes
menores que podem ser reaproveitadas. isso simplifica a 
codifição.

Estrutura função em python

def nome_funcao(param1, param2, paramN):
    //algum código que a função faz 
    return valor_retornado

'''

#cria uma funcão que calcula a área fo triângulo
def calculateTriangleArea(base, altura):
    area = (base * altura) / 2
    return area

#cria uma funcão que calcula a área fo triângulo
def calculateSquareArea(lado):
    area = lado * lado
    return area

'''
#Exemplo 1: chamar a função
area1 = calculateTriangleArea(100, 10)
print("A área do triângulo 1 é ", area1)

#Exemplo 2: Chamar a funcao novamente
base = float(input('Digita a base: '))
altura = float(input('Digita a altura: '))
area2 = calculateTriangleArea(base, altura)
print("A área do triâgulo 2 é ", area2)
'''

