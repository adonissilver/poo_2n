
class Curso:
    def __init__(self, cod_curso, nome, modalidade):
        self.cod_curso = cod_curso
        self.nome = nome
        self.modalidade = modalidade


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
