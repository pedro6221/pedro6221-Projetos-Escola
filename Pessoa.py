class SerVivo:
     
     def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

class Pessoa(SerVivo):

    def andar(self):
        print(f"{self.nome} está andando...")

    def estudar(self):

        print(f"{self.nome} pessoa está estudando...")

    def dormir(self):
        print(f"{self.nome} pessoa está dormindo...")
        
    def i(self):
        print(f"{self.nome} tem {self.idade} anos de idade")
    
# p1=Pessoa("João Pedro",17)
p1=Pessoa(input("digite seu nome:"),int(input("digite sua idade: ")))

p1.estudar()
p1.andar()
p1.dormir()
p1.i()