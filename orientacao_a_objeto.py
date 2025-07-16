#Introdução a orientação a objeto
#Exemplo simples 01

class carro :
    def __init__(self, modelo, cor):
        self.modelo = modelo 
        self.cor = cor 
        self.velocidade = 0 #o carro começa parado

#acelerar o carro aumentando sua velocidade com incrementos personalizados
    def acelerar(self, incremento):
        self.velocidade += incremento 
        print(f'O carro {self.modelo} da cor {self.cor} acelerou para {self.velocidade}km/h. ')

#DESAFIO EM SALA - REDUZIR A VELOCIDADE:
    def reduzir(self, decremento):
        self.velocidade -= decremento 
        print(f'O carro {self.modelo} da cor {self.cor} reduziu para {self.velocidade}km/h. ')

#Parar o carro, tornando sua velocidade 0.
    def parar(self):
        self.velocidade = 0 #só um igual nesse caso pq é uma igualdade e nao esta comparando nada
        print(f'O carro {self.modelo} da cor {self.cor} parou bruscamente. ')

#Cria um objeto carro
meu_carro01 = carro('Fusca', 'Amarelo')
meu_carro02 = carro('SJ', 'Preto')
#incrementos/decrementos:
meu_carro01.acelerar(20) #Acelerar o carro a 20km/h
meu_carro02.acelerar(20)
meu_carro01.parar()
meu_carro02.reduzir(5)
