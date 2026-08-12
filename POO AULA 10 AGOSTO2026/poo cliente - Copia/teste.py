from cliente import Cliente


print("=== Cadastro de Cliente ===")

id = int(input("Digite o ID: "))
nome = input("Digite o nome: ")
contato = int(input("Digite o contato: "))
endereco = input("Digite o endereço: ")

cliente = Cliente(id, nome, contato, endereco)

print("\n=== Dados do Cliente ===")
cliente.exibir_dados()


