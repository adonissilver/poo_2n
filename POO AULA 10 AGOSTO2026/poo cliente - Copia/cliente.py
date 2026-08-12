class Cliente:
    def __init__(self, id: int, nome: str, contato: int, endereco: str):
        self.id = id
        self.nome = nome
        self.contato = contato
        self.endereco = endereco

    def exibir_dados(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Contato: {self.contato}")
        print(f"Endereço: {self.endereco}")