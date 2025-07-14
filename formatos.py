# Detalhando Strings e usando formato

nomeCompleto = "Alice Python Pierce"
inicio = 5
fim = inicio + 6

'''
#colchete serve para como se fosse um recorte pelo que eu entendi - nesse caso ele esta selecionando os caracteres
print(nomeCompleto[6:11])

print(nomeCompleto[inicio:fim])
'''
'''
nome = input("Qual seu nome?")
sobrenome = input("Qual seu sobrenome?")
print("Seu nome completo é: " + nome + " " + sobrenome)
'''
#OBS: coloquei as 3 aspas para ocultar pq quis fazer outra operacao sem isso ai antes

#OBS2: coloquei int para que os numeros virarem str e somirem, 
#ao inves de 2 mais dois virar 22, ele vira 4 que é o correto
#str faz numero virar texto, e int faz texto virar numero
caixinha01 = int(input("Insira seu primeiro valor: "))
caixinha02 = (input("Insira seu segundo valor: "))
resultado = caixinha01 + int(caixinha02)
print("Total: " + str(resultado))
print("Total:",str(resultado)) #opcao 2, usando virgula - nao precisa dar espaco e nem transoformar em str!!!
#O FINAL É TEXTO ; para contas nao é o ideal

