from pessoa import Pessoa

def main():
    #1.Criando um objeto com dados inseridos diretamente
    p1= Pessoa("Douglas Almendro",40,"111.222.333-44","douglas@email.com",5000.00)
    p1.exibir_dados();

#2 Criando um objeto com dados vindos do usuário
print("--- Cadastro de Nova Pessoa --- ")
nome_in = input("Nome: ")
idade_in= int(input("Idade: "))
cpf_in = input("CPF: ") 
email_in = input("E-mail")
renda_in = float(input("Renda: "))

p2= Pessoa(nome_in, idade_in,cpf_in,email_in,renda_in)
p2.exibir_dados()




if __name__ == "__main__":
    main()