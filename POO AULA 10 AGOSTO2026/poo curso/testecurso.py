



from curso import Curso

print("=== Cadastro de Curso ===")

id = int(input("Digite o ID: "))

nome = input("Digite o nome do curso: ")

duracao = int(input("Digite a duração do curso em meses: "))

mensalidade = float(input("Digite o valor da mensalidade: "))

curso = Curso(id, nome, duracao, mensalidade)

print("\n=== Dados do Curso ===")

curso.exibir_dados()