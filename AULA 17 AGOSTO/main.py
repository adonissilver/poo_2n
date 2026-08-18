#PROCEDIMENTO DE IMPORTACAO:
#SINTAXE : from nome_do_arquivo import NomeDaClasse
from pessoa import Pessoa

def main():
    
    #1.Crianco um objeto com dados inseridods diretamento
    p1 = Pessoa("Douglas Almendro",40,"111.222.333-44","douglas@email.com")

    #2.Criando um objeto com dados vindos do usuário
    print ("--Cadastro de Nova Pessoa")
    nome_in = input("Nome: ")
    idade_in = int(input("Idade: "))
    cpf_in =  input("CPF: ")
    email_in = input("E-mail: ")

    p2 = Pessoa(nome_in,idade_in,cpf_in,email_in)
    #3.Usando os objetos
    print("\n-- Resultados ---")
    p1.exibir_dados()
    p2.exibir_dados()

#Execucao principal
if __name__ == "__main__":
    main()