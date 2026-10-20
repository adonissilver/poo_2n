class Disciplina:
    def __init__(self, cod_disciplina, nome, carga, cod_professor, cod_curso):
        self.cod_disciplina = cod_disciplina
        self.nome = nome
        self.carga = carga
        self.cod_professor = cod_professor
        self.cod_curso = cod_curso


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