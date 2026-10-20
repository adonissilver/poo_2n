from aluno import Aluno
from principal import Curso, Disciplina, Professor

def CadastrarCurso(curso):
    with open("cursos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{curso.cod_curso},{curso.nome},{curso.modalidade}\n"
        )


def main():
    print("=== CADASTRO DE CURSO ===")

    cod_curso = input("Digite o código do curso: ")
    nome = input("Digite o nome do curso: ")
    modalidade = input("Digite a modalidade do curso: ")

    curso = Curso(cod_curso, nome, modalidade)

    CadastrarCurso(curso)
    print("\nCurso cadastrado com sucesso!")


if __name__ == "__main__":
    main()
    
def CadastrarAluno(Aluno):
    with open("alunos.txt", "a") as arquivo:
        arquivo.write(f"{Aluno.matricula},{Aluno.nome},{Aluno.CPF},{Aluno.email},{Aluno.cod_curso}\n")
            
def main():
    print("=== CADASTRO DE Aluno ===")

    matricula = input("Digite a matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    CPF = input("Digite o CPF do aluno: ")
    email = input("Digite o email do aluno: ")
    cod_curso = input("Digite o código do curso: ")

    aluno = Aluno(matricula, nome, CPF, email, cod_curso)

    CadastrarAluno(aluno)

    print("\nAluno cadastrado com sucesso!")


if __name__ == "__main__":
    main()


def CadastrarDisciplina(disciplina):
    with open("disciplinas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{disciplina.cod_disciplina},{disciplina.nome},{disciplina.carga},{disciplina.cod_professor},{disciplina.cod_curso}\n"
        )

def main():
    print("=== CADASTRO DE DISCIPLINA ===")

cod_disciplina = input("Digite o código da disciplina: ")
nome = input("Digite o nome da disciplina: ")
carga = input("Digite a carga da disciplina: ")
cod_professor = input("Digite o código do professor responsável: ")
cod_curso = input("Digite o código do curso ao qual a disciplina pertence: ")

disciplina = Disciplina(cod_disciplina, nome, carga, cod_professor, cod_curso)

CadastrarDisciplina(disciplina)

print("\ndisciplina cadastrada com sucesso!")


if __name__ == "__main__":
    main()
    

def CadastrarProfessor(professor):
    with open("professor.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{professor.codigo},{professor.nome},{professor.CPF},{professor.especialidade}\n"
        )


def main():
    print("=== CADASTRO DE PROFESSOR ===")

    codigoProfessor = input("Digite o código do professor: ")
    nome = input("Digite seu nome: ")
    CPF = input("Digite o CPF: ")
    especialidade = input("Digite sua especialidade: ")

    professor = Professor(codigoProfessor, nome, CPF, especialidade)

    CadastrarProfessor(professor)

    print("\nProfessor cadastrado com sucesso!")


if __name__ == "__main__":
    main()