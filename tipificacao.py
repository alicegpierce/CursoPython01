"""Trabalhando com Tipificações e variáveis"""

nome  = "Alice"
print(nome)
print(nome)

sobrenome = 'Pierce' #isso é uma string (ou seja, tipo um corpo de texto)
idade = 23 #sem as aspas, se nao ele soma os numeros unindo-os (integer - numeros inteiros)
altura = 1.65 #float (valores decimais)
bermuda = False #boolean (sim/nao)

print(nome + " " + sobrenome)
print(nome + " " + sobrenome + "tem" +str(idade) + "anos")
print(nome + " " + sobrenome +  " " + "tem"  + " " +str(idade)  + " " + "anos") #add espaco como texto
print(idade + 2)

textoVariasLinhas = '''
esse é um texto 
de várias 
linhas
'''
print(textoVariasLinhas)
