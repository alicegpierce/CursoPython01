#Trabalhando com loopings

palavra = "garrafinha"
contador = 1 #fora das aspas pq quero que contador seja um numero
print("Palavra Escolhida: ", palavra)
for letra in palavra : #poderia substituir letra por x, i , o que quiser, é uma incógnita, uma variável
    print(contador, " - ", letra)
    contador = contador + 1 

cidades = ['São Paulo', 'Santa Fé Do Sul', 'Londres', 'Campinas', 'Santa Cruz', 'Portland', 'Nashville' ]

for cidade in cidades :  #nunca comecar uma variavel com numero!! crime!!
    print(cidade)

print(cidades [2])

print("---------- While ----------")

botaoExecutar = True #valor boolean
contador = 0 
while botaoExecutar :
    print(contador)
    contador = contador + 1 
    if contador >= 10 : 
        botaoExecutar = False 
print("fim da lista")

print('\n') #fiz para pular a linha

print('----- Exercicio 01: -----')
listaCompras = ['Leite', 'Ovos', 'Iogurte', 'Filé mignon', 'Arroz', 'Suco', 'Cenoura', 'Biscoito de polvilho', 'Presunto crú', 'Manteiga', 'Chocolate']
contador = 1 
for item in listaCompras : 
    print('[',contador,']' , '-', item) #se eu quisesse fazer com + eu mudaria para str (exemplo abaixo)
    contador = contador + 1
print("fim da lista")

print('\n') #fiz para pular a linha

print('----- Exercicio 01.2 (Utilizando + & str): -----')
listaCompras = ['Leite', 'Ovos', 'Iogurte', 'Filé mignon', 'Arroz', 'Suco', 'Cenoura', 'Biscoito de polvilho', 'Presunto crú', 'Manteiga', 'Chocolate']
contador = 1 
for item in listaCompras : 
    print('['+ str(contador) + ']' , '-', item) #se eu quisesse fazer com + eu mudaria para str (exemplo abaixo)
    contador = contador + 1
print("fim da lista")

