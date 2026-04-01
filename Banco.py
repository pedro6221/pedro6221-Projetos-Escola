class Cartao:
    def __init__(self,cvc=None,num=None,dono=None):
        if num is None:
            
            num=str(input("Digite o número de seu cartão: "))
        
        if dono is None:
            
            dono=str(input("Digite o nome que está no cartão: "))
            
        if cvc is None :
            cvc=str(input("Digite o cvc do seu cartão: "))
            
            while len(cvc)!=3:
                
                print("Código inválido")
                
                cvc=str(input("Digite o cvc do seu cartão: "))
                
        self.cvc=cvc
        self.num=num
        self.dono=dono
    
    def comprar(self):
        print(f"Compra realizada com o cartão de {self.dono}")
        print(f"Número do cartão: {self.num}")
        print(f"CVC: {self.cvc}")

class Nubank(Cartao):
    def __init__(self, cvc=None, num=None, dono=None, limite:float=None):
        super().__init__(cvc, num, dono)
        
        if limite is None:
            limite=float(input("Digite o limite do seu cartão Nubank: "))
        
        self.limite=limite
    
    def comprar(self):
        compra= float(input("Qual preço da compra? R$ "))
        if compra > self.limite:
            print("Compra não autorizada. Limite insuficiente.")
        
        else:  
            print(f"Compra realizada com o cartão Nubank de {self.dono}")
            print(f"Número do cartão: {self.num}")
            print(f"CVC: {self.cvc}")
            print(f"Limite disponível: R$ {self.limite:.2f}")

class Inter(Cartao):
    def __init__(self, cvc=None, num=None, dono=None, cashback=None):
        super().__init__(cvc, num, dono)
        
        if cashback is None:
            cashback=float(input("Digite o percentual de cashback do seu cartão Inter: "))
        
        self.cashback=cashback
    
    def comprar(self):
        compra= float("Qual preço da compra? R$ ")
        desconto= compra * (self.cashback / 100)
        valorf= compra - desconto
        
        print(f"Compra realizada com o cartão Inter de {self.dono}")
        print(f"Número do cartão: {self.num}")
        print(f"CVC: {self.cvc}")
        print(f"Cashback aplicado: R$ {desconto:.2f}")
        print(f"Valor final da compra: R$ {valorf:.2f}")

class Bradesco(Cartao):
    def __init__(self, cvc=None, num=None, dono=None, pontos=None):
        super().__init__(cvc, num, dono)
        
        if pontos is None:
            pontos=int(input("Digite a quantidade de pontos do seu cartão Bradesco: "))
        
        self.pontos=pontos
    
    def comprar(self):
        compra= float("Qual preço da compra? R$ ")
        pontosg= int(compra // 10)
        self.pontos += pontosg
        
        print(f"Compra realizada com o cartão Bradesco de {self.dono}")
        print(f"Número do cartão: {self.num}")
        print(f"CVC: {self.cvc}")
        print(f"Pontos ganhos nesta compra: {pontosg}")
        print(f"Total de pontos acumulados: {self.pontos}")

class Next(Cartao):
    def __init__(self, cvc=None, num=None, dono=None, anuidade=None):
        super().__init__(cvc, num, dono)
        
        if anuidade is None:
            anuidade=float(input("Digite o valor da anuidade do seu cartão Next: "))
        
        self.anuidade=anuidade
    
    def comprar(self):
        compra= float("Qual preço da compra? R$ ")
        
        print(f"Compra realizada com o cartão Next de {self.dono}")
        print(f"Número do cartão: {self.num}")
        print(f"CVC: {self.cvc}")
        print(f"Anuidade do cartão: R$ {self.anuidade:.2f}")

class Santander(Cartao):
    def __init__(self, cvc=None, num=None, dono=None, beneficios=None):
        super().__init__(cvc, num, dono)
        
        if beneficios is None:
            beneficios=input("Digite os benefícios do seu cartão Santander: ")
        
        self.beneficios=beneficios
    
    def comprar(self):
        compra= float("Qual preço da compra? R$ ")
        
        print(f"Compra realizada com o cartão Santander de {self.dono}")
        print(f"Número do cartão: {self.num}")
        print(f"CVC: {self.cvc}")
        print(f"Benefícios do cartão: {self.beneficios}")

class Itau(Cartao):
    def __init__(self, cvc=None, num=None, dono=None, limite=None):
        super().__init__(cvc, num, dono)
        
        if limite is None:
            limite=float(input("Digite o limite do seu cartão Itaú: "))
        
        self.limite=limite
    
    def comprar(self):
        compra= float("Qual preço da compra? R$ ")
        if compra > self.limite:
            print("Compra não autorizada. Limite insuficiente.")
        
        else:  
            print(f"Compra realizada com o cartão Itaú de {self.dono}")
            print(f"Número do cartão: {self.num}")
            print(f"CVC: {self.cvc}")
            print(f"Limite disponível: R$ {self.limite:.2f}")

def comprar(cartao):
    cartao.comprar()

# c=Cartao()
nu=Nubank()
# i=Inter()
# b=Bradesco()
# n=Next()
# it=Itau()
# s=Santander()
# comprar(c)
comprar(nu)
# comprar(i)
# comprar(b)
# comprar(n)
# comprar(it)
# comprar(s)