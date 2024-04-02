'''Crie um programa que imprime uma tabuada. O programa deve solicitar 
que o usuário informe um número para gerar a tabuada. Utilizando um 
laço de repetição, o programa deve gerar a tabuada do número 
fornecido de 0 a 100.'''


'''Questao 3'''

n1 = int(input("Qual o numero: "))


for i in range(0, 101):
    resultado = n1 * i
    print(f"{n1} x {i} = {resultado}")


