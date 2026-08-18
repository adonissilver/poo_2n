class Pessoa:
    #CONSTRUTOR DA CLASSE PESSOA
    def __init__ (self,nome,idade,cpf,email):
            
        #ATRIBUTOS
        self.nome = nome 
        self.idade =idade 
        self.cpf = cpf 
        self.email = email 

    #metodo para apresentar os dados da pessoa
    def exibir_dados(self):
        print(f"Nome: {self.nome},Idade:{self.idade},CPF:{self.cpf},Email{self.email}" )
