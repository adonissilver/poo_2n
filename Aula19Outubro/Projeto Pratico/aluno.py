class Aluno:
    def __init__(self, matricula, nome, CPF, email, cod_curso):
        self.matricula = matricula
        self.nome = nome
        self.CPF = CPF
        self.email = email
        self.cod_curso = cod_curso
        
        
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
