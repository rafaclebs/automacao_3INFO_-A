'''
Exercício 1:
 Crie um programa que lê dois número
 inteiros do teclado e após imprime 
 o maior números dentre eles.
'''

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))


if num1 > num2:
    maior_numero = num1
else:
    maior_numero = num2


print("O maior número é:", maior_numero)