#Calculadora Básica em Python

def intro() :
    return r'''
  _                                  
 /   _. |  _     |  _.  _|  _  ._ _. 
 \_ (_| | (_ |_| | (_| (_| (_) | (_| 

---FEITO POR ALICE

    '''

def mostrar_menu() :
    return '''
        [1] ou [+] para Somar
        [2] ou [-] para Subtrair
        [3] ou [/] para Dividir
        [4] ou [*] para Multiplicar
        [5] para Sair
        (ou digite sua opção: Somar / Subtrair / Multiplicar / Dividir / Sair)
        '''

#funcao que lê os valores
def ler_valores() :
    valor01 = int(input('Insira o primeiro valor: '))
    valor02 = int(input('Insira o segundo valor: '))
    return valor01, valor02

def somar(a ,b) :
    return a + b 
def subtrair(a ,b) :
    return a - b 
def dividir(a ,b) : #teremos um bug quando divisivel por 0
    return a / b
def multiplicar(a ,b) :
    return a * b 

#funcao para permanecer ou sair do programa
def desejacontinuar() :
    print('''
          [1] Não, desejo sair!
          [2] Sim, desejo realizar outro cálculo.
          ''')
    opcao = input('Deseja realizar outra conta? ')
    return opcao != '1'

#Looping principal
executar = True
print(intro())
while executar : 
    print(mostrar_menu())
    operador = input('Selecione a sua opção: ').strip().lower()

    if operador in ['5', 'sair']: 
        print('Obrigado por usar a melhor calculadora!')
        break

    v01, v02 = ler_valores() 

    if operador in ['1', '+', 'somar'] :
        resultado = somar(v01, v02)
    elif operador in ['2', '-', 'subtrair'] :
        resultado = subtrair(v01, v02)
    elif operador in ['3', '/', 'dividir'] :
        resultado = dividir(v01, v02)
    elif operador in ['4', '*', 'multiplicar'] :
        resultado = multiplicar(v01, v02)
    else :
        print('Opção inválida. Tente novamente.')
        continue

    print('Resultado: ' + str(resultado))
    executar = desejacontinuar()

