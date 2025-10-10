class Casa:
    def __init__(self,cor=None,quartos=None,banheiro=None,tamanho=None):
    #SELF SERVE PARA DECLARAR QUE A VARIÁVEL É UM OBJETO
    #NONE SERVE PARA DAR UM VALOR NULO AO OBJETO
        self.cor=cor
        self.quarto=quartos
        self.banheiro=banheiro
        self.tamanho=tamanho
        
    def descrever(self):
        #APRENDI QUE POSSSO DECLARAR VALORES QDO O PROGRAMA ESTÁ RODANDO E NAO SÓ NO FINAL
        
        self.cor=str(input("Qual é a cor de sua casa? "))
        
        self.quarto=int(input("Quantos quartos tem sua casa? "))
        
        self.banheiro=int(input("Quantos banheiros tem sua casa? "))
        
        self.tamanho=float(input("Qual tamanho de sua casa em m²? "))
        
        return f"Essa casa é da cor {self.cor}, tem {self.quarto} quartos, {self.banheiro} banheiros e tem {self.tamanho} m² "
        
# C=Casa()
# print(C.descrever())

class Pessoa:
    def __init__(self,Nome=None,idade=None):
        self.nome=Nome
        self.idade=idade
        self.nome=str(input("Qual é seu nome? "))
        self.idade=int(input("Quantos anos você tem? "))
    
    def falar(self,mensagem=None):#esse mensagem é útil?
        self.mensagem=mensagem
        self.mensagem=str(input("Oque você quer falar? "))
        
        return f"{self.nome} disse: {self.mensagem}"
    
    def cantar(self):#NÃO PRECISO BOTAR VARIÁVEIS AQUI NOS PARÊNTESES
        self.musica=str(input("Qual música você está cantando? "))
        self.cantor=str(input("Quem é o cantor(a) dessa música? "))
        
        return f"{self.nome} está cantando {self.musica}"
    
    def estudar(self):
        self.materia=str(input("Qual matéria você está estudando? "))
        
        return f"{self.nome} está estudando {self.materia}"
    
    def bio(self):
        return f"Meu nome é {self.nome} tenho {self.idade} anos gostaria de falar {self.mensagem}, eu gosto de cantar {self.musica} do cantor {self.cantor} e estou estudando a matéria {self.materia}"
    
p=Pessoa()
p.falar()
p.cantar()
p.estudar()
print(p.bio())  #SÓ VAI MOSTRAR O RETURN MAS SE CASO EU QUISESSE MOSTRAR OS OUTROS RETURNS TERIA Q FAZER [print(p.falar())]     
print(p.falar()) #SÓ TEMOS QUE COLOCAR NA ORDEM CERTA, NO CASO APARECEU ISSO:
#Oque você quer falar? ola
#jp disse: ola
#MAS ISSO SÓ ACONTECEU NO FINAL PQ COLOQUEI ELA DEPOIS DE TODAS AS FUNÇÕES
        
            