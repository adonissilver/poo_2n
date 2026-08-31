from pessoa import Pessoa 
def main():
    # Agora esta linha vai funcionar, pois passamos 4 dados e a classe aceita 4
    p1 = Pessoa("Douglas Almendro", 40, "111.222.333-44", "douglas@email.com")
    
    print("--- Cadastro de Nova Pessoa ---")
    nome_in = input("Nome: ")
    
    try:
        idade_in = int(input("Idade: "))
    except ValueError:
        idade_in = 0
        
    cpf_in = input("CPF: ")
    email_in = input("E-mail: ")
    
    # Criando o segundo objeto
    p2 = Pessoa(nome_in, idade_in, cpf_in, email_in)

    print("\n--- Resultados ---")
    p1.exibir_dados()
    p2.exibir_dados()

if __name__ == "__main__":
    main()