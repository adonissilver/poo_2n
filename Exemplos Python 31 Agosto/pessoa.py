class Pessoa:
    # AJUSTE: Agora aceitamos nome, idade, cpf e email (total 5 com o self)
    def __init__(self, nome=None, idade=0, cpf=None, email=None):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf      # Importante: precisa guardar o CPF
        self.email = email  # Importante: precisa guardar o Email

    # AJUSTE: Adicionando o método que o main tenta chamar
    def exibir_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | CPF: {self.cpf} | Email: {self.email}")

