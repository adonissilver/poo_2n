class Aluno:
    def __init__(self, matricula, nome, CPF, email, cod_curso):
        self.matricula = matricula
        self.nome = nome
        self.CPF = CPF
        self.email = email
        self.cod_curso = cod_curso

class Curso:
    def __init__(self, cod_curso, nome, modalidade):
        self.cod_curso = cod_curso
        self.nome = nome
        self.modalidade = modalidade
        
class Disciplina:
    def __init__(self, cod_disciplina, nome, carga, cod_professor, cod_curso):
        self.cod_disciplina = cod_disciplina
        self.nome = nome
        self.carga = carga
        self.cod_professor = cod_professor
        self.cod_curso = cod_curso
        
class Professor:
    def __init__(self, codigoProfessor, nome, CPF, especialidade):
        self.codigo = codigoProfessor
        self.nome = nome
        self.CPF = CPF
        self.especialidade = especialidade
