# Gerencia cursos, alunos e inscrições. Permite listar cursos disponíveis, inscrever alunos, registrar a 
# conclusão de cursos e gerar certificados simples. Pode incluir categorias de cursos e progresso do 
# aluno

"""
Nome:
    - Caio Bertochi Rodrigues
    - Lucas Germano
"""
# Criação de classe

class Aluno:

    def __init__(self, nome, email, curso):
        self.__nome = nome
        self.__email = email
        self.__curso = curso

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def lista_curso(self):
        return self.__curso

    def set_nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            raise ValueError("Não registrado")

    def gerar_certificado(self):
        print("Certificado da faculdade - APROVADO")
        print(f"Nome: {self.get_nome()}")
        print(f"Email: {self.get_email()}")
        print(f"Curso: {self.lista_curso()}")
        print("-----")


class AlunoGraduacao(Aluno):
    def gerar_certificado(self):
        print("Certificado de Graduação")
        print(f"Parabéns {self.get_nome()}!")
        print(f"Curso concluído: {self.lista_curso()}")
        print("-----")

class AlunoPosGraduacao(Aluno):
    def gerar_certificado(self):
        print("Certificado de Pós-Graduação")
        print(f"{self.get_nome()} concluiu com sucesso o curso de {self.lista_curso()}")
        print("-----")
# Criação da segunda classe
class Inscrição:

    def __init__(self):
        self.usuarios = []
# Criação de objetos
    def cadastrar_aluno(self, nome, email, curso, tipo="normal"):
        try:
            if tipo == "graduacao":
                novo = AlunoGraduacao(nome, email, curso)
            elif tipo == "pos":
                novo = AlunoPosGraduacao(nome, email, curso)
            else:
                novo = Aluno(nome, email, curso)
            self.usuarios.append(novo)
            print("Aluno cadastrado!")

        except ValueError as erro:
            print(f"Erro detectado: {erro}")

    def listar_alunos(self):
        for usuario in self.usuarios:
            usuario.gerar_certificado()
# Execução
aluno1 = Inscrição()
aluno1.cadastrar_aluno("alan", "alan@gmail.com", "Inglês", tipo="graduacao")
aluno1.listar_alunos()

aluno2 = Inscrição()
aluno2.cadastrar_aluno("Roberto", "roberto@icloud.com", "Informática", tipo="pos")
aluno2.listar_alunos()

aluno3 = Inscrição()
aluno3.cadastrar_aluno("Mariana", "mariana@icloud.com", "Francês", tipo="normal")
aluno3.listar_alunos()

