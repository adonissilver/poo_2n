class Pessoa:
    # CONSTRUTOR
    def __init__(self, nome, idade, cpf, email,renda):
        # ATRIBUTOS
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.renda=renda

    # MÉTODO
    def exibir_dados(self):
        print(f"Nome: {self.nome }\n Idade: {self.idade}\n  CPF: {self.cpf}" )
        print(f"  E-mail: {self.email}\n  Renda: {self.renda}")

    



