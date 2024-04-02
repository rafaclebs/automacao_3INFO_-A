'''Crie um programa que imprima mensagens motivacionais dependendo do 
horário do dia. O programa deve solicitar a hora atual. Se a hora estiver 
entre 8 e 10, o programa deve imprimir “Bom dia! Você consegue alcançar 
seus objetivos!”. Se a hora estiver entre 10 e 14, imprimir “Hora do almoço! 
Recarregue suas energias para continuar avançando!”. Se estiver entre 14 
e 17, imprimir “Boa tarde! Persista nos seus esforços, você está no caminho 
certo!”.'''



'''Questao 2'''

hora = int(input("Que horas é "))

if hora >= 8 and hora < 10:
    print("Bom dia! Você consegue alcançar seus objetivos!")
elif hora >= 10 and hora < 14:
    print("Hora do almoço! Recarregue suas energias para continuar avançando!")
elif hora >= 14 and hora < 17:
    print("Boa tarde! Persista nos seus esforços, você está no caminho certo!")
else:
        print("Não há mensagem motivacional para este horário.")
