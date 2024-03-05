'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''


grupo1 = []
grupo2 = []
grupo3 = []


while True:
    matricula = int(input("Digite o número de matrícula (digite 0 para parar): "))
    
  
    if matricula == 0:
        break
    

    if matricula % 3 == 0:
        grupo3.append(matricula)
    elif matricula % 2 == 0:
        grupo2.append(matricula)
    else:
        grupo1.append(matricula)


print("Grupo 1:", grupo1)
print("Grupo 2:", grupo2)
print("Grupo 3:", grupo3)