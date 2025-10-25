class Veiculo:
    def __init__(self, tipo=None, marca=None, cor=None):
        self.tipo = tipo
        self.marca = marca
        self.cor = cor

    def comprar(self):
        if self.tipo is None:
            esc = True
            while esc:
                esc = int(input("""
                    Você quer comprar um veículo?
                    [1] - Sim
                    [2] - Não
                    """))
                if esc == 2:
                    break

                    while True:
                        tipo = int(input("""
                        Digite o tipo do veículo:
                        [1] - Carro
                        [2] - Moto
                        [3] - Caminhão
                        """))

                        if tipo == 1:
                            tipo = "Carro"
                        elif tipo == 2:
                            tipo = "Moto"
                        elif tipo == 3:
                            tipo = "Caminhão"

                        marca = input("Digite a marca do veículo: ")
                        cor = input("Digite a cor do veículo: ")

                        if len(cor) > 0:
                            self.tipo = tipo
                            self.marca = marca
                            self.cor = cor
                            print("Veículo comprado com sucesso!")
                            esc = False
                            break
                        else:
                            print("Cor inválida, tente novamente.")
    
     def exibir(self):
        if self.tipo:
            print(f"Veículo: {self.tipo} | Marca: {self.marca} | Cor: {self.cor}")
        else:
            print("Nenhum veículo cadastrado.")


class User(Veiculo):
    def __init__(self, user=None, senha=None):
        super().__init__()
        if user is None:
            user = input("Digite seu usuário: ")

        if senha is None:
            senha = input("Digite sua senha: ")

        self.user = user
        self.__senha = senha

    def comprar(self):
        super().comprar()


class Admin(User):
    def __init__(self, user=None, senha=None):
        super().__init__(user, senha)
    
    
        if user is None:
                user = input("Digite seu usuário: ")

        if senha is None:
         senha = input("Digite sua senha: ")

        self.user = user
        self.__senha = senha
        

    def comprar(self):
        super().comprar()
    
    def remover_veiculo(self):
        self.tipo = None
        self.marca = None
        self.cor = None
        print("Veículo removido com sucesso!")



