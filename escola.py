#Trabalhando com if e testes

'''
!= diferente
== Igual
<= Menor ou igual
>= Maior ou igual
< Menor
> Maior
'''

tipoEscola = input("Tipo do Colégio: \n [1] Público \n [2] Particular \n ")
freqAluno = input("Frequência do aluno: ")
nomeAluno = input("Nome do aluno: ")
mediaAluno = int(input("Média do aluno: "))  #coloquei int porque decidi fazer a media da escola como 7,
#se nao eu nao precisava colocar
#mediaEscola = input("Média de corte da escola: ") coloquei como comentario pq decidi ja colocar a nota
mediaEscola = 7
freqAluno = int(freqAluno)


if tipoEscola == "2": 
    print("----- Colégio Particular -----")
    if mediaAluno >= mediaEscola and freqAluno >=70 :
        print("APROVADO")
    else:
        print("REPROVADO")

if tipoEscola == "1":
    print("----- Colégio Público -----")
    if mediaAluno >= mediaEscola or freqAluno >=60 :
        print("APROVADO")
    else:
        print("REPROVADO")
    