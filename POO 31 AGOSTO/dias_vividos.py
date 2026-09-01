
def calcular_dias(dia,mes,ano):
    total=dia+(mes*30)+(ano*12*30)
    return total

def solicita_dados():
    dia=int(input("Digite o dia que voce nasceu: "))
    mes=int(input("Digite o número do mês você nasceu: "))
    ano=int(input("Digite o ano do seu nascimento: "))
    return(dia,mes,ano)



def main():
    solicita_dados()
    calcular_dias()


if __name__=="__main__":
    main()




