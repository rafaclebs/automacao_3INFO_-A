'''Crie uma função chamada "limparTela". Essa função não deve receber 
parâmetros. No arquivo "funcao.py", você deve importar o módulo "os" 
(“import os”). Dentro da função "limparTela", você vai utilizar a função 
"system" do módulo "os" para executar o comando ‘cls’, que limpa a tela 
no Windows (por exemplo: os.system('cls')). No arquivo principal, você 
deve imprimir uma mensagem ‘Limpando a tela’, após chamar a função 
"limparTela", e depois imprimir outra mensagem ‘Nova mensagem em 
tela limpa’.'''

'''Questao 4'''

from funcao import limparTela

print("Chamando a função para limpar a tela...")
limparTela()
print("Nova mensagem em tela limpa")