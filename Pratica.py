class Pessoa:

     def __init__(self, nome, idade, salario):

         self.nome = nome
         self.idade = idade
         self.salario = salario

     def i(self):

         if self.salario <= 1400.00:

             self.salario += self.salario * 0.1

             print(f"Novo salário: {self.salario}"  )

         else:

             self.salario -= self.salario * 0.05

             print(f"Novo salário: {self.salario}"  )

         if self.idade >= 18:

             print(f"{self.nome} você é maior de idade")

         else:

             print(f"{self.nome} você é menor de idade")




p1= Pessoa(str(input("digite seu nome: ")),int(input("digite sua idade: ")),float(input("digite seu salário: ")))
p1 = Pessoa("JP", 17, 1200)

p1.i()