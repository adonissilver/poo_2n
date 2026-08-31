#Média de Notas: Crie um programa que receba 3 notas de um aluno, 
# calcule a média aritmética e exiba o resultado.



def main():
    nota1_in = float(input("Digite a primeira nota: "))
    nota2_in = float(input("Digite a segunda nota: "))
    nota3_in = float(input("Digite a terceira nota: "))
    media(nota1_in, nota2_in, nota3_in)

if __name__ == "__main__":
    main()

def media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(f"A média do aluno é: {media}:.2f")


