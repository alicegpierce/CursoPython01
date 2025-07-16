#Trabalhando com orientação a objeto e polimorfismo

class Animal :
    def comunicar(self): 
        pass

class Cachorro(Animal):
    def comunicar(self):
        return 'au au'

class Gato(Animal):
    def comunicar(self):
        return 'miau'
    
#Usando o polimorfismo
def fazer_animal_falar(animal: Animal):
    print(animal.comunicar())

#Criando os objetos, nesse caso os animais
cachorro = Cachorro()
gato = Gato()

#Chamando o método de cada animal de forma polimórfica
fazer_animal_falar(cachorro)
fazer_animal_falar(gato)

