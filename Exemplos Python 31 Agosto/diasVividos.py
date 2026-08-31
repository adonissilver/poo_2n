from datetime import date # Importa a classe date da biblioteca datetime

class CalculadoraDatas:
    def __init__(self, dia, mes, ano):
        # Converte os dados recebidos em um objeto de data do Python
        # Se os números forem inválidos (ex: dia 31 de fevereiro), o Python gerará um erro aqui
        self.data_informada = date(ano, mes, dia)

    def calcular_diferenca(self):
        # Captura a data atual do sistema
        data_hoje = date.today()
        
        # Realiza a subtração das datas. O resultado é um objeto chamado 'timedelta'
        diferenca = data_hoje - self.data_informada
        
        # Retornamos apenas a propriedade .days (o número de dias)
        # abs() garante que o número seja positivo mesmo se a data for no futuro
        print(f"\nA quantidade de dias entre {diferenca.days}")
              

        return abs(diferenca.days)

def main():
    print("=== Contador de Dias até Hoje ===")
    
    try:
        # 1. Coleta de dados
        d = int(input("Digite o dia: "))
        m = int(input("Digite o mês: "))
        a = int(input("Digite o ano: "))

        # 2. Instanciação da classe
        calc = CalculadoraDatas(d, m, a)

        # 3. Cálculo e exibição
        total_dias = calc.calcular_diferenca()
        
        data_formatada = f"{d}/{m}/{a}"
        print(f"\nA quantidade de dias entre {data_formatada} e hoje é de: {total_dias} dias.")

    except ValueError:
        # Esse erro ocorre se o usuário digitar letras ou uma data impossível (como 30/02)
        print("\nErro: Data inválida! Verifique se os números estão corretos.")

if __name__ == "__main__":
    main()