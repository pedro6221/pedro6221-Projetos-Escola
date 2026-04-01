# class Conta: 
#     def __init__(self, saldo=0):
#         self.__saldo=saldo
        
    
#     @property
#     def saldo(self):
#         return self.__saldo
    
#     @saldo.setter
#     def saldo(self, valor):
#         if valor < 0:
#             print("Saldo não pode ser negativo.")
#         else:
#             self.__saldo=valor
    
#     def depositar(self, valor):
#         if valor > 0:
#             self.__saldo += valor
        
# conta2=Conta(500)
# print("Saldo inicial:", conta2.saldo)

# conta2.saldo = -300
# print("Saldo após tentativa de ajuste:", conta2.saldo)

# conta2.depositar(300)
# print("Saldo após depósito:", conta2.saldo)

class Aluno:
    def __init__(self, nota=0):
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, valor):
        if valor < 0:
            print("Nota não pode ser negativa.")
        elif valor > 10:
            print("Nota não pode ser maior que 10.")
        else:
            self.__nota = valor


# Interação com o usuário
print("Bem-vindo ao sistema de notas!")

# Criar um aluno com nota inicial fornecida pelo usuário
nota_inicial = float(input("Digite a nota inicial do aluno: "))

while nota_inicial < 0 or nota_inicial > 10:
    
    print("Nota inválida. A nota deve estar entre 0 e 10.")
    nota_inicial = float(input("Digite a nota inicial do aluno: "))
    
aluno1 = Aluno(nota_inicial)

print("Nota inicial:", aluno1.nota)

# Tentar ajustar a nota
nova_nota = float(input("Digite a nova nota do aluno: "))

aluno1.nota = nova_nota

print("Nota após tentativa de ajuste:", aluno1.nota)

# Ajustar novamente com outra nota
nova_nota = float(input("Digite outra nova nota do aluno: "))

aluno1.nota = nova_nota

print("Nota após ajuste válido:", aluno1.nota)