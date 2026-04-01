class Profissoes:
    def __init__(self,nome=None,cpf=None,idade=None):
        
     if nome is None and cpf is None and idade is None:
        def id(self):
            nome=input("Digite seu nome ")
            cpf=input("Digite seu cpf ")
            idade=input("Digite sua idade ")
            self.nome=nome
            self.cpf=cpf
            self.idade=idade
        
        
    
    def salario(self):
        print("Salário base da profissão.")
    
    def trabalhar(self):
        print("Trabalhando na profissão.")

class Medico:
    def salario(self):
        print("O salário do médico é R$ 15.000,00.")
    
    def trabalhar(self):
        print("O médico está atendendo pacientes.")

class Engenheiro:
    def salario(self):
        print("O salário do engenheiro é R$ 10.000,00.")
    
    def trabalhar(self):
        print("O engenheiro está projetando uma construção.")
        
class Professor:
    def salario(self):
        print("O salário do professor é R$ 1.000,00.")

    def trabalhar(self):
        print("O professor está ensinando alunos.")

class Programador:
    def salario(self):
        print("O salário do programador é R$ 100,00 bruto.")

    def trabalhar(self):
        print("O programador está escrevendo código.")

def salario(poli):
    poli.salario()

pro=Profissoes()
M=Medico()
E=Engenheiro()
P=Professor()
Pr=Programador()

salario(M)
salario(E)
salario(P)
salario(Pr)

print("\n" + "-"*200)

for loop in (Profissoes(),Medico(),Engenheiro(),Professor(),Programador()):
    loop.salario()
  
print("\n" + "-"*200)
  
for loop2 in (Profissoes(),Medico(),Engenheiro(),Professor(),Programador()):
    loop2.trabalhar()
