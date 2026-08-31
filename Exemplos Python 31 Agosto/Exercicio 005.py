def calcular_tabuada(numero):
    """Função que recebe um número e imprime sua tabuada de 1 a 10."""
    print(f"\n--- Tabuada do {numero} ---")
    i=0
    # O range(1, 11) gera números de 1 até 10 (o 11 não entra)
    for i in range(0, 11):
        resultado = numero * i
        # Exibição formatada: Ex: 5 x 1 = 5
        print(f"{numero} x {i:2} = {resultado}")
    
    print("-" * 20)

def main():
    print("=== Gerador de Tabuada ===")
    
    try:
        # 1. Coleta o número do aluno
        num_escolhido = int(input("Digite o número que deseja multiplicar: "))
        
        # 2. Chama a função para processar e exibir a tabuada
        calcular_tabuada(num_escolhido)
        
    except ValueError:
        # Tratamento de erro caso o aluno digite algo que não seja número
        print("Erro: Por favor, digite apenas números inteiros válidos.")

if __name__ == "__main__":
    main()