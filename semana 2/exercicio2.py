'''
Exercício 2:
Crie um programa que lê do teclado a nota
e a quantidade de faltas de um aluno. O
programa deve imprimir reprovado, se:
A nota for menor que 6 ou se as presencas
forem menor do que 75 e aprovado 
caso contrário.
'''


nota = float(input("Digite a nota do aluno: "))
faltas = int(input("Digite a precenca do aluno: "))


if nota > 6 or faltas > 75:
    print("Aprovado")
else:
    print("Reprovado")