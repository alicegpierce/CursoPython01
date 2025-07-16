import json, requests 

nome = input('Qual o seu nome? ')
localidade = 0 

while localidade < 1 or localidade > 2:
    localidade = int(input('Você deseja selecionar uma localidade? \n[1] Sim \n[2] Não \n'))

if localidade == 1:
    uf = input('Qual UF deseja buscar? \n[35] SP \n[33] RJ \n[31] MG \n[43] RS \n[53] DF \n')
    resultado = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}?localidade={uf}')

if localidade == 2:  #brasil inteiro, sem selecionar UF
    uf = input('Qual UF deseja buscar? \n[35] SP \n[33] RJ \n[31] MG \n[43] RS \n[53] DF \n')
    resultado = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}') #por isso nao tem localidade no domínio como no primeiro if

print('''
    [1] - 1930
    [2] - 1930 a 1940
    [3] - 1940 a 1950
    [4] - 1950 a 1960
    [5] - 1960 a 1970
    [6] - 1970 a 1980
    [7] - 1980 a 1990
    [8] - 1990 a 2000
    [9] - 2000 a 2010
  ''')

periodo = int(input('Selecione o periodo: ')) - 1 #subtraimos 1 porque a contagem na programacao sempre começa em 0, entao se eu nao subtraisse, ao selecionar por exemplo a faixa 6, iria me mostrar os dados da faixa 7.
dados = json.loads(resultado.text)
print(dados[0]['res'][periodo]) #esse 'res' é de resources
