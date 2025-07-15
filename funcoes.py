# Entendendo funções em Python
# uma funcao seria onde, por exemplo, "guarda" o código

def minhaFuncao() : 
    print('Olá Mundo')

'''
minhaFuncao()
minhaFuncao()
minhaFuncao()
minhaFuncao()
''' #coloquei aspas para virar texto agora só pq nao queria que aparecesse quando eu rodasse os proximos exs da aula

alunos = ['Jesreel', 'Eloara', 'Emily', 'Alice', 'Andressa', 'Davi']
cursos = ['Python', 'PHP', 'SQL']

'''
# Trabalhando com variáveis de funcao 
def minhaFuncaoMelhorada(animal): #animal poderia ser substituido por X ou a variavel da minha preferencia
    print('Você gosta de '+ str(animal)) #poderia usar só virgula, mas coloquei + e str() que prefiro

petCliente = input('Qual seu animal preferido? ')
minhaFuncaoMelhorada(petCliente)
minhaFuncaoMelhorada('iguana')
''' #coloquei como texto ''' para seguir no prox exercicio


'''
#MELHORANDO:
def minhaFuncaoMelhorada(animal, primaveras): #animal poderia ser substituido por X ou a variavel da minha preferencia
    print('Você gosta de '+ str(animal) + ' e ele tem ' + primaveras , 'anos') #poderia usar só virgula, mas coloquei + e str() que prefiro

petCliente = input('Qual seu animal preferido? ')
idadePet = input('Qual a idade do seu' + ' ' + str(petCliente) + '? ')
minhaFuncaoMelhorada(petCliente, idadePet)
minhaFuncaoMelhorada('iguana', '4')
''' #coloquei como texto ''' para seguir no prox exercicio

def funcaoIdade(nascimento, anoatual):
    print('Você tem', anoatual - nascimento, 'anos')
nascimento = int(input('Insira seu ano de nascimento: '))
anoatual = int(input('Ano atual: '))
funcaoIdade(nascimento, anoatual)
#exercicio no arquivo idade.py!!!! correcao e continuacao
