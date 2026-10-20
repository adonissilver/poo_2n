
class professor:
    def __init__(self, codigoProfessor, nome, CPF, especialidade):
        self.codigo = codigoProfessor
        self.nome = nome
        self.CPF = CPF
        self.especialidade = especialidade

    def CadastrarProfessor(self):
        with open("professor.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(
                f"{self.codigo},{self.nome},{self.CPF},{self.especialidade}\n"
            )


def main():
    print("=== CADASTRO DE PROFESSOR ===")

    codigoProfessor = input("Digite o código do professor: ")
    nome = input("Digite seu nome: ")
    CPF = input("Digite o CPF: ")
    especialidade = input("Digite sua especialidade: ")

    professor_obj = professor(codigoProfessor, nome, CPF, especialidade)

    professor_obj.CadastrarProfessor()

    print("\nProfessor cadastrado com sucesso!")


if __name__ == "__main__":
    main()
