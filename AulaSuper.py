class Pessoa:
    def __init__(self,nome:str,cpf:int)-> None :
        self.nome=nome
        self.cpf=cpf
        
    def apresentar(self) -> str:
        return f"Olá,eu sou {self.nome} e tenho CPF {self.cpf}"
    
class Aluno(Pessoa):
    def __init__(self,nome : str,matricula:str,cpf:int) -> None:
        super().__init__(nome,cpf)
        self.matricula=matricula
        
        
        
        def apresentar(self) ->str:
            base= super().apresentar()
            return f"{base} e sou aluno, matricula {self.matricula}"

class Professor(Pessoa,Aluno):
    def __init__(self, nome: str, cpf: int,matricula: str )-> None:
        super().__init__(nome, cpf)
        super().__init__(matricula)
    
    def apresentar(self)->str :
        base=super().apresentar()
        return f"{base} e eu sou Professor"

p=Pessoa("Joao",1234567890)
a=Aluno("ana","A456",12345332112)
pr=Professor("Mario",12345555554,"A765")

print(p.apresentar())
print(a.apresentar())     
print(pr.apresentar())   
# class Professor(Pessoa):
#     def __init__(self, nome: str,disciplina:str,cpf:int) -> None:
#         super().__init__(nome)
#         super().__init__(cpf)
#         self.disciplina=disciplina
        
#     def apresentar(self) ->str :
#         return f"Professor {self.nome} de {self.disciplina}"
    
# class BolsaMixin:
#     def calcular_bolsa(self)-> float:
#         return 1200
    
# class AlunoBolsista(BolsaMixin,Aluno):
#     def apresentar(self) ->str:
#         base=super().apresentar()
#         return f"{base} e recebo bolsa de R$ {self.calcular_bolsa():.2f}"
    
# def apresentar_todos(pessoas: list[Pessoa]) -> list[str]:
#     return [p.apresentar() for p in pessoas]

# def main()->None:
#     p=Pessoa("João",3456776543)
#     a=Aluno("Ana",'A123',9876556789)
#     pr=Professor("Carlos","Matemática",123454321)
#     ab=AlunoBolsista("Beatriz","B456",1234567890)
    

    
    # resultados= apresentar_todos([p,a,pr,ab])
    # for r in resultados:
    #     return r
    
    # print("",
    #       f"isintance(ab, Pessoa): {isinstance(ab, Pessoa)}",
    #       f"isintance(ab, Aluno): {isinstance (ab, Aluno)}",
    #       f"isintance(ab, BolsaMixin): {isinstance (ab, BolsaMixin)}",
    #       sep='\n')
    
    # print("MRO AlunoBolsista: ")
    # for cls in AlunoBolsista.__mro__:
    #     print(" -", cls.__name__)
        
    # if __name__=="__main__":
    #  main()
    
        
        
        
    