# ============================
#   CLASSE BASE
# ============================

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf      # privado
        self._tipo = "Pessoa" # protegido

    def apresentar(self):
        print(f"{self._tipo}: {self.nome}, {self.idade} anos.")

    def get_cpf(self):
        return self.__cpf     # acesso controlado


# ============================
#   CLASSE ESCOLA
# ============================

class Escola(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)
        self._tipo = "Membro da Escola"


# ============================
#   ALUNO
# ============================

class Aluno(Escola):

    def __init__(self, nome, idade, cpf, matricula, turma):
        super().__init__(nome, idade, cpf)
        self.matricula = matricula
        self.turma = turma
        self.notas = []
        self.frequencia = 100

    def mostrar_menu(self):
        opcoes = {
            1: self.ver_notas,
            2: self.ver_frequencia
        }
        self.executar_menu(opcoes)

    def ver_notas(self):
        print(f"Notas de {self.nome}: {self.notas if self.notas else 'Nenhuma nota cadastrada.'}")

    def ver_frequencia(self):
        print(f"Frequência do aluno {self.nome}: {self.frequencia}%")

    def executar_menu(self, opcoes):
        while True:
            try:
                for k,v in opcoes.items():
                    print(f"[{k}] - {v.__name__.replace('_',' ').capitalize()}")
                escolha = int(input("Escolha: "))
                if escolha in opcoes:
                    opcoes[escolha]()
                    break
            except:
                print("Entrada inválida.")


# ============================
#   PROFESSOR
# ============================

class Professor(Escola):
    def __init__(self, nome, idade, cpf, materia):
        super().__init__(nome, idade, cpf)
        self.materia = materia

    # ---------- Métodos úteis ----------
    def calcular_media(self, notas):
        return sum(notas) / len(notas)

    def registrar_notas(self):
        aluno = input("Nome do aluno: ")
        notas = [float(input(f"Nota {i+1}: ")) for i in range(4)]
        media = self.calcular_media(notas)

        if media >= 6:
            print(f"{aluno} passou com média {media}.")
        elif 5 <= media < 6:
            print(f"{aluno} em recuperação com média {media}.")
        else:
            print(f"{aluno} reprovou com média {media}.")

    def dar_aviso(self):
        aviso = input("Digite o aviso: ")
        print(f"Professor {self.nome} avisou: {aviso}")

    # ---------- Menu ----------
    def mostrar_menu(self):
        opcoes = {
            1: lambda: print("Mostrando alunos..."),
            2: self.registrar_notas,
            3: self.dar_aviso
        }
        self.executar_menu(opcoes)

    def executar_menu(self, opcoes):
        while True:
            try:
                for k,v in opcoes.items():
                    print(f"[{k}] - {v.__name__.replace('_',' ').capitalize()}")
                escolha = int(input("Escolha: "))
                if escolha in opcoes:
                    opcoes[escolha]()
                    break
            except:
                print("Entrada inválida.")



# ============================
#   COORDENADOR (HERDA PROFESSOR)
#   Usa polimorfismo — sobrescreve menu
# ============================

class Coordenador(Professor):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf, materia="Gerência")

    def ligar_pais(self):
        aluno = input("Nome do aluno: ")
        print(f"Ligando para os pais de {aluno}...")

    def suspender(self):
        aluno = input("Aluno: ")
        dias = int(input("Dias de suspensão: "))
        print(f"{aluno} suspenso por {dias} dias.")

    def expulsar(self):
        aluno = input("Aluno: ")
        print(f"{aluno} foi expulso.")

    def advertencia(self):
        aluno = input("Aluno: ")
        print(f"{aluno} recebeu advertência.")

    # Polimorfismo: substitui menu do Professor
    def mostrar_menu(self):
        opcoes = {
            1: self.ligar_pais,
            2: self.suspender,
            3: self.expulsar,
            4: self.advertencia
        }
        self.executar_menu(opcoes)


# ============================
#   BIBLIOTECA
# ============================

class Biblioteca(Escola):
    def __init__(self, nome, idade, cpf, vagas):
        super().__init__(nome, idade, cpf)
        self.vagas = vagas

    def alugar_livro(self):
        livro = input("Livro: ")
        print(f"Livro {livro} alugado com sucesso!")

    def reservar_sala(self):
        qtd = int(input("Quantas vagas reservar? "))
        if self.vagas + qtd > 20:
            print("Limite ultrapassado.")
        else:
            self.vagas += qtd
            print("Vagas reservadas!")

    def ver_vagas(self):
        print(f"Vagas ocupadas: {self.vagas}/20")

    def mostrar_menu(self):
        opcoes = {
            1: self.alugar_livro,
            2: self.reservar_sala,
            3: self.ver_vagas
        }
        self.executar_menu(opcoes)

    def executar_menu(self, opcoes):
        while True:
            for k,v in opcoes.items():
                print(f"[{k}] - {v.__name__.replace('_',' ').capitalize()}")
            try:
                escolha = int(input("Escolha: "))
                if escolha in opcoes:
                    opcoes[escolha]()
                    break
            except:
                print("Opção inválida.")



# ============================
#   DIRETORIA
# ============================

class Diretoria(Escola):

    def demitir(self):
        nome = input("Funcionário: ")
        print(f"{nome} foi demitido.")

    def criar_regra(self):
        regra = input("Nova regra: ")
        print(f"Regra criada: {regra}")

    def ver_pendencias(self):
        print("Listando pendências...")

    def expulsar(self):
        aluno = input("Aluno: ")
        motivo = input("Motivo: ")
        print(f"Aluno {aluno} expulso. Motivo: {motivo}")

    def mostrar_menu(self):
        opcoes = {
            1: self.demitir,
            2: self.criar_regra,
            3: self.ver_pendencias,
            4: self.expulsar
        }
        self.executar_menu(opcoes)

    def executar_menu(self, opcoes):
        while True:
            try:
                for k,v in opcoes.items():
                    print(f"[{k}] - {v.__name__.capitalize()}")
                escolha = int(input("Escolha: "))
                if escolha in opcoes:
                    opcoes[escolha]()
                    break
            except:
                print("Inválido.")



