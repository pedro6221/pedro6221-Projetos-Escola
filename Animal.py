class Animal:

    def __init__(self,nome):

        self.nome=nome
     
    def falar(self):

        print("Som do animal")

class Cachorro(Animal):

    def falar(self):

        print("vai se fuder!")

class Gato(Animal):

    def falar(self):

        print("afim de errar hoje!")


dog= Cachorro("caramelo")

cat=Gato("terrorista")



print("***************************************************************************************")

dog.falar()

cat.falar()    

    



