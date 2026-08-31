def main():
    print("=== Sistema Acadêmico ===")
    
    # 1. Coleta a nota do usuário
    nota = float(input("Digite a nota final do aluno (0 a 10): "))

    # 2. COMANDO DE DECISÃO SIMPLES
    # Se a condição (nota >= 6) for verdadeira, executa o primeiro bloco.
    if nota >= 6.0:
        print("Resultado: ALUNO APROVADO!")
        print("Parabéns pelo esforço.")
    
    # Se a condição for falsa, o Python pula para o 'else'
    else:
        print("Resultado: ALUNO REPROVADO.")
        print("É necessário estudar mais para a recuperação.")

    print("\nFim do processamento.")

if __name__ == "__main__":
    main()