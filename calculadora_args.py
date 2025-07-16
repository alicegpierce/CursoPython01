#Calculadora com múltiplos argumentos


class Calculadora:
    def somar(self, *args): #esse asterisco nesse caso significa TUDO, ou seja, nesse caso, todos argumentos que estao dentro dele mesmo - nao indica multiplicacao - nada a ver!!!
        return sum(args)
calc = Calculadora()

#Passagem dos argumentos (Quantos desejar)
print(calc.somar(2,6)) #Retorna 8
print(calc.somar(1,2,3,4,5)) #Retorna 15
