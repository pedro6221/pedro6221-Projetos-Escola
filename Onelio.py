class Onelio:
    def __init__(self,nome=None,serie=None,turma=None,escola=None,cpf=None,matricula=None):
        self.nome=nome
        self.serie=serie
        self.turma=turma
        self.escola=escola
        self.__cpf=cpf #OBJETO PRIVADO
        self._matricula=matricula #OBJETO PROTEGIDO
        
        
    
    def detalhes(self):
        self.escola=str("Qual nome da escola que você é matriculado?")
        self._matricula=int("Qual sua matrícula?")
        
        self.nome=str(input("Digite seu nome: "))
        self.serie=int(input("Qual sua série? "))
        self.turma=str(input("Qual sua turma? "))
        
a=Onelio()
print(a.detalhes())
        
        
        