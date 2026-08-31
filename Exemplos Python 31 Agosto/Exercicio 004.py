def verificar_situacao():
    print("=== Portal do Aluno: Verificação de Notas ===")
    
    try:
        # 1. Entrada de dados
        nota = float(input("Digite a nota final (0.0 a 10.0): "))

        # 2. ESTRUTURA DE DECISÃO COMPOSTA
        
        # Condição 1: Nota para aprovação direta
        if nota >= 6.0:
            print("\nSituação: APROVADO")
            print("Parabéns! Você atingiu a média necessária.")
            
        # Condição 2: Nota entre 4.0 e 5.9 (Recuperação/Exame)
        # O 'elif' só é testado se o 'if' lá de cima for Falso
        elif nota >= 4.0:
            print("\nSituação: EXAME (Recuperação)")
            print("Você ainda tem uma chance. Estude para a prova de exame!")
            
        # Condição 3: Tudo o que for menor que 4.0
        else:
            print("\nSituação: REPROVADO")
            print("Infelizmente sua nota foi insuficiente para o exame.")

    except ValueError:
        print("Erro: Digite uma nota válida usando ponto para decimais (Ex: 5.5).")

def main():
    verificar_situacao()
    print("\nSistema encerrado.")