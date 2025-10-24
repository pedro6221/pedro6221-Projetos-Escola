class Veiculo:
    def __init__(self,tipo=None,marca=None,cor=None):
        def comprar(self):
            if tipo is None:
                
                esc=True
                while esc==True: 
                    esc=int(input("""
                            Você quer comprar um veículo?
                            [1]-Sim
                            [2]-Não
                            """))
                    if esc==2:
                        break
                    
                    if esc==1:
                        
                        while True:
                            tipo=int(input("""
                                    Digite o tipo do veículo:
                                    [1]-Carro
                                    [2]-Moto
                                    [3]-Caminhão"""))
                            
                            if tipo==1:
                                tipo="Carro"
                            
                            if tipo==2:
                                tipo="Moto"
                            
                            if tipo==3:
                                tipo="Caminhão"
                            
                            marca=input("Digite a marca do veículo: ")
                            cor=input("Digite a cor do veículo: ")
                            
                            if len(cor)>0:
                                
                                self.tipo=tipo
                                self.marca=marca
                                self.cor=cor
                                break
                                
                                esc=False
                            else:
                                return comprar()



class User(Veiculo):
    def __init__(self,user=None,senha=None):
        
        if user is None:
            user=input("Digite seu usuário: ")
        
        if senha is None:
            senha=input("Digite sua senha: ")
        
        self.user=user
        self.__senha=senha
    
    def comprar(self):
            super().comprar()



class Admin(User):
    def __init__(self, user=None, senha=None):
        
        if user is None:
            user=input("Digite seu usuário: ")
        
        if senha is None:
            senha=input("Digite sua senha: ")
            
        super().__init__(user, senha)
        
    def comprar(self):
            super().comprar()

            