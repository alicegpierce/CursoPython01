#Importar o modulo unittest que nos permite escrever testes automatizados
import unittest 

#Importar as funções de teste
from teste_unitario import somar, subtrair, multiplicar, dividir

#Criar a classe quem contem os testes unitários para as funções de operação
class TesteOperacoes(unittest.TestCase):
    #testar a função de soma
    def testar_soma(self):
        #verificar se a soma de 2 e 3 é igual a 5
        self.assertEqual(somar(2,3),5)
        #verificar se a soma de 1 e -1 é igual a 0
        self.assertEqual(somar(-1,1),0)
        #verificar se a soma de -2 e -3 é igual a -5
        self.assertEqual(somar(-2,-3),-5)

    def testar_divisao(self):
        self.assertEqual(dividir(6,2),3)
        self.assertEqual(dividir(-6,3),-2)
        self.assertEqual(dividir(-6,-2),3)
        with self.assertRaises(ValueError):
            dividir(1,0) #vai dar erro quando realizar o teste pois não é possível dividir por zero
        
    def testar_multiplicaco(self):
        self.assertEqual(multiplicar(1,2),2)
        self.assertEqual(multiplicar(-5,2),-10)
        self.assertEqual(multiplicar(-10,-3),30)

    def testar_subtracao(self):
        self.assertEqual(subtrair(9,2),7)
        self.assertEqual(subtrair(5,-1),6)
        self.assertEqual(subtrair(-3,-2),-1)



#permite que os testes sejam executados quando rodamos o arquivo diretamente
if __name__ == '__main__':
    unittest.main() #executa todos os testes definidos na classe
