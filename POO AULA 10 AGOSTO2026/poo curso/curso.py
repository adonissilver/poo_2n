class Curso:
    def __init__(self, id: int, nome: str, duracao: int, mensalidade: float):
        self.id = id
        self.nome = nome
        self.duracao = duracao
        self.mensalidade = mensalidade

    def exibir_dados(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Duração: {self.duracao} meses")
        print(f"Mensalidade: R$ {self.mensalidade:.2f}")

