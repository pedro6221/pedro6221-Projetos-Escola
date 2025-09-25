class Escola:
    def __init__(self,nome,idade,cpf):
        self.nome=nome
        self.idade=idade
        self.cpf=cpf
        # self.turma=turma
        
        
class Aluno(Escola):

    def idAluno(self,matricula,turma):

        self.matricula=matricula
        self.turma=turma

        print(f"o aluno {self.nome} com matrícula {self.matricula} está na turma {self.turma} ")

        esc=0

        while esc not in[1,2]:

            esc=int(input(f"{self.nome} o que você quer fazer agora?\n[1]-para ver as notas;\n[2]-para ver a frequencia\n"))

            if esc == 1:

                print("vendo notas...")

            elif esc == 2:

                print("vendo a fequência...")


class Professor(Escola):

    def idProf(self,materia):

        self.materia=materia

        print(f"o professor {self.nome} tem {self.idade} está lecionando a turma do Onélio com a matéria de {self.materia}")

        esc=0
        while esc not in [1,2,3]:

            esc=int(input(f"Professor {self.nome} o que você quer fazer agora? \n [1]-Ver seus alunos\n [2]-colocar notas do aluno\n [3]-dar aviso para os alunos\n"))
        
            if esc==1:

                print("Vendo os alunos...")
        
            if esc==2:

                nome=str(input("Qual aluno você quer colocar a nota? "))

                n1=float(input("digite a primeira nota do aluno "+nome+": "))

                n2=float(input("digite a segunda nota do aluno "+nome+": "))

                n3=float(input("digite a terceira nota do aluno "+nome+": "))

                n4=float(input("digite a quarta nota do aluno "+nome+": "))
            
                media=(n1+n2+n3+n4)/4

                if media >=6:

                    print("O aluno "+ nome + " está com média "+ str(media)+" e passou na matéria "+ self.materia)

                if media >=5 and media <=6:
                    
                    esc2=0
                    while esc2 not in [1,2,3]:

                        esc2=int(input("O aluno "+ nome + " está com média "+ str(media)+" você deseja \n[1]-arredondar\n[2]-passar um trabalho\n[3]-fazer recuperação\n"))

                        if esc2==1:

                            print("Nota do aluno "+nome+" foi arredondada e ele passou de ano")

                        if esc2==2:

                            print("O aluno "+nome+" irá fazer um trabalho")

                        if esc2==3:

                            dia=str(input("o aluno "+nome+" irá fazer recuperação que dia? "))

                            print("Prova de recuperação marcada para o dia: "+dia)
                
                if media<5:
                   
                   print("O aluno "+ nome + " está com média "+ str(media)+" e reprovou na matéria  "+ self.materia)

            if esc==3:

                avs=str(input("Qual aviso você deseja falar? "))

                print("o professor "+self.nome+" Avisou que:\n"+avs)

class Coordenador(Escola): #class Coordenador(Escola,Professor):
    def idCoor(self):
        
        esc=0
        while esc not in [1,2,3,4]:

            esc=int(input(f"Bom dia {self.nome} oque você deseja fazer? \n [1]-Para ligar para os pais do aluno\n[2]-para suspender o aluno\n[3]-para expulsar o aluno\n[4]-para dar advertência no aluno\n"))

            if esc==1:

                nome=str(input("Qual pai de aluno você quer ligar? "))

                print(f"ligando para os pais do aluno {nome}")

            if esc==2:

                nome=str(input("Qual aluno você quer suspender? "))

                dias=int(input(f"Quantos dias você quer suspender o aluno {nome} ? "))

                print(f"o aluno {nome} foi suspenso por {dias} dias ")
            
            if esc==3:

                nome=str(input("Qual aluno você quer expulsar? "))

                print(f"o aluno {nome} foi expulso ")
            
            if esc==4:
                 
                 nome=str(input("Qual aluno você quer dar advertência? "))

                 print(f"o aluno {nome} levou uma advertência ")

class Responsavel(Escola):

    def idResp(self):

        esc=0
        while esc not in [1,2,3,4]:
            esc=int(input(f"Bom dia {self.nome} oque você deseja fazer?\n[1]-para ver as notas do aluno\n[2]-ligar para o coordenador\n[3]-para justificar a falta do aluno\n[4]-pedir transferência do aluno\n"))
        
            if esc==1:
                nome=str(input("Qual nome do seu filho? "))
                print(f"vendo as notas do aluno {nome} ")

            if esc==2:
                print("Ligando para o coordenador...")
        
            if esc==3:

                nome=str(input("Qual nome do seu filho? "))

                mtv=str(input(f"Qual o motivo da falta do aluno {nome}? "))

                print(f"O aluno {nome} faltou porque: {mtv}")
            
            if esc==4:

                nome=str(input("Qual nome do seu filho? "))

                esc2=0
                while esc2 not in [1,2]:

                    esc2=int(input("Você já tem uma escola para transferir?\n [1]-Sim\n[2]-Não\n"))

                    if esc2==1:

                        mudar=str(input(f"Qual escola você quer transferir o aluno {nome}? "))

                        print(f"o aluno {nome} foi transferido para a escola {mudar} ")

                    if esc2==2:

                        print(f"procurando escola para o aluno {nome}")

class Biblioteca(Escola):
    def idBibl(self,vagas):
        self.vagas=vagas

        esc=0
        while esc not in [1,2,3]:

            esc=int(input("Bom dia, oque você deseja fazer agora?\n [1]-alugar um livro\n[2]-reservar sala da biblioteca\n[3]-verificar vagas na biblioteca\n"))

            if esc==1:

                livro=str(input("Qual livro você quer alugar? "))

                dia=int(input("Que dia que você quer alugar esse livro? "))

                if dia==31:
                    dia=1

                mes=int(input("Que mês você quer alugar esse livro? "))

                if mes==12:
                    mes=1

                mesf=mes+1

                print(f"Você alugou o livro {livro} e terá que entregar dia {dia} do mês {mesf}")
                
            if esc==2:

                qtd=int(input("Quantas vagas você quer reservar? "))

                self.vagas=self.vagas+qtd

                if self.vagas>20:

                    print("Não foi possível reservar a vaga...")

                else:
                    
                    print(f"{qtd} reservadas...")

            if esc==3:
                    
                    print(f"A sala tem {self.vagas} vagas reservadas ")

class Secretaria(Escola):
    def idSecr(self):

        esc=0
        
        while esc not in[1,2,3]:
            
            esc=int(input("Oque você deseja fazer?\n [1]-fazer impressões\n[2]-fazer declaração\n[3]-informar algum problema\n"))
            
            if esc==1:
                
                esc2=0
                while esc2 not in[1,2,3,4]:

                    esc2=int(input("Oque você deseja imprimir?\n[1]-atividade\n[2]-provas\n[3]-trabalho\n[4]-outro\n"))

                    if esc2==1:

                        qtd=int(input("Quantas cópias você quer? "))

                        print(f"fazendo {qtd} cópias de atividade...")

                    if esc2==2:

                        qtd=int(input("Quantas cópias você quer? "))

                        print(f"fazendo {qtd} cópias de provas...")

                    if esc2==3:

                        qtd=int(input("Quantas cópias você quer? "))

                        print(f"fazendo {qtd} cópias do trabalho...")

                    if esc2==4:

                        nome=str(input("Oque você quer fazer? "))

                        qtd=int(input("Quantas cópias você quer? "))

                        print(f"fazendo {qtd} cópias de {nome}...")

            if esc==2:
                print("fazendo declaração...")
            
            if esc==3:
                nome=str(input("Que problema você quer informar? "))

                print(f"Problema informado com sucesso! ")

class Cantina(Escola):
    def idCantina(self):
        esc=0
        while esc not in [1,2]:

            esc=int(input("Deseja ver o cardápio do dia?\n[1]-Sim\n[2]-Não "))

            if esc==1:
                print("cardápio do dia:\nSegunda:Creme de galinha\nTerça:Carne cozida\nQuarta:Frango assado\nQuinta:Carne oriental\nSexta:Feijoada")
            if esc==2:
                break

class Quadra():

    def idQuadra():
        esc=0
        while esc not in[1,2]:
    
            esc=int(input("Deseja ver a quadra do dia?\n[1]-Sim\n[2]-Não \n"))

            if esc==2:
                break
            
            if esc==1:
                print("Segunda:ADM1\nTerça:FIN1\nQuarta:DS1\nQuinta:ENF1\nSEXTA:DS2")
                break

class Financeiro(Escola):
    def idFin(self):

        esc=0
        while esc not in[1,2,3]:
            
            esc=int(input("O que você deseja fazer?\n[1]-Ver finanças da escola\n[2]-Ver contas a pagar\n[3]-Pagar contas\n"))

            if esc==1:
                print("Vendo finanças...")

            if esc==2:
                print("Vendo as contas...")
            
            if esc==3:
                print("Pagando as contas...")

class Segurança(Escola):
    def idSeg(self):
        esc=0
        while esc not in[1,2]:
    
            esc=int(input("Deseja ver o segurança do dia?\n[1]-Sim\n[2]-Não \n"))

            if esc==2:
                break
            
            if esc==1:
                print("Segunda:Roberto\nTerça:Gabriel\nQuarta:betuca\nQuinta:Veggeti\nSEXTA:Cristiano R.")
                break

class Diretoria(Escola):
    def idDir(self):
        esc=0
        while esc not in [1,2,3,4]:

            esc=int(input("Oque você quer fazer?\n[1]-para demitir funcionário \n[2]-Fazer uma regra\n[3]-verificar pendências \n[4]-expulsar aluno\n "))

            if esc==1:

                nome=str(input("Qual funcionário você quer demitir? "))

                print(f"o funcionário {nome} foi demitido...")

            if esc==2:

                regra=str(input("Qual regra você deseja adicionar? "))

                print(f"Nova regra adicionada agora a regra {regra} deverá ser seguida")
            
            if esc==3:

                print("Vendo pendências...")
            
            if esc==4:

                nome=str(input("Qual aluno você quer expulsar? "))

                mtv=str(input("Qual motivo dessa expulsão? "))

                print(f"O aluno {nome} foi expulso\n motivo: {mtv}")

# ----------- Testes -----------


# p1=Coordenador("Jp","17","123456789")
# p1.idCoor()


# p2=Aluno("Maria",16,"987654321")
# p2.idAluno("12345","DS2")

# p3=Professor("Carlos",40,"111222333")
# p3.idProf("Matemática")

# p4=Responsavel("Carmem",40,"121212121")
# p4.idResp()

# p5=Biblioteca("Rapunzel",34,"1231231231")
# p5.idBibl(10)

# p6=Secretaria("Lucas",42,"121243434545")
# p6.idSecr()

# p7=Cantina("Marcio",42,"12345789")
# p7.idCantina()

# p8=Quadra                     #Nao precisa botar parentese qdo nao herda nada e qdo nao tem variavel
# p8.idQuadra()

# p9=Financeiro("Roberto",27,"123456789")
# p9.idFin()

# p10=Segurança("Betuca",70,121212121212)
# p10.idSeg()

# p11=Diretoria("Ronaldo",67,21212123344)
# p11.idDir()





#João Pedro DS2