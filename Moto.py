class Moto:
    def __init__(self, modelo, ano, cor, vel):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = vel

    def acelerar(self, val):

        self.velocidade += val

        print(f"a moto {self.modelo} acelerou para {self.velocidade} km/h")
    
    def frear(self, val):
        self.velocidade -= val

        if self.velocidade < 0:

            self.velocidade = 0

        print(f"a moto {self.modelo} desacelerou para {self.velocidade} km/h")

    def detalhes(self):
        
        return f"{self.modelo}  ({self.ano}) - Cor: {self.cor}, Velocidade: {self.velocidade} km/h"
    
M1 = Moto("pop100", 2015, "prata", 43)
M2 = Moto("Bros", 2019, "rosa", 54)

M1.acelerar(20)
M2.acelerar(20)

M1.frear(40)
M2.frear(40)

print(M1.detalhes())
print(M2.detalhes())

if M1.velocidade > M2.velocidade:

    print(f"a moto {M1.modelo} está mais rápida que {M2.modelo} diferença de {M1.velocidade - M2.velocidade} km/h")

elif M1.velocidade < M2.velocidade:

    print(f"a moto {M2.modelo} está mais rápida que {M1.modelo} diferença de {M2.velocidade - M1.velocidade} km/h")

else:

    print(f"a moto {M1.modelo} está na mesma velocidade que {M2.modelo} com {M1.velocidade} km/h")


