# Exercicio: IDADE
# Perguntar ano de nascimento e o atual, retornar idade e perguntar se deseja novo teste

#o que o professor fez: (beem diferente do que eu fiz em funcoes.py rs)
# Ex.01:
'''
executar = True
while executar :
    anoNasc = int(input('Em que ano você nasceu? '))
    anoAtual = int(input('Em que ano estamos? '))
    idade = anoAtual - anoNasc
    print('Você tem ' + str(idade) + ' anos.')
    opcao = input('\nDeseja tentar novamente? \n [1]Sim \n [2]Não \n')
    if opcao == '2' :
        executar = False
'''

print('----- Exercício 02 Usando Funções -----')

def calcular_idade() :
    anoNsc = int(input('Em que ano você nasceu? '))
    anoAtl = int(input('Em que ano estamos? '))
    idade = anoAtl - anoNsc
    print('Você tem ' + str(idade) + ' anos.')

def perguntar_novamente() :
    opcao = input('Deseja testar novamente? Sim ou Não')
    if opcao.lower() in ['sim', 's', 'sm', 'si', 'simm', 'im', 'sin', 'sn', 'in']  :
        iniciarprograma()
    else : 
        print('Encerrando programa! Até mais!')

def iniciarprograma() :
    calcular_idade()
    perguntar_novamente()

#Chamada inicial
iniciarprograma()