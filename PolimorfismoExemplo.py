class Pato:
    def quack(self):
        print("Quack!")

class Pessoa:
    def quack(self):
        print("Estou imitando um pato: Quack!")
    
    def comer(self):
        print("Estou comendo.")

def fazer_quack(sla):
    sla.quack()

p=Pato()
h=Pessoa()
fazer_quack(p)
fazer_quack(h)

class Gravacao:
    def quack(self):
        print("Gravando som de pato: Quack!")

class Robo:
    def quack(self):
        print("Robô imitando pato: Quack!")


objetos = [Pato(), Pessoa(), Gravacao(), Robo()]

for classe in objetos:
    classe.quack()
