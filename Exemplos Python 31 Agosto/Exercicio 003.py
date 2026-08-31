def area_do_triangulo(base, altura):
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area}")
def perimetro_do_triangulo(ladoA, ladoB, ladoC):
    perimetro = (ladoA + ladoB + ladoC)
    print(f"O perímetro do triângulo é: {perimetro}")
def main():
    print("_" * 50)
    print("--- Cálculos em triângulos ---")
    print("*" * 50)
    # É bom usar um try/except para o caso de o usuário não digitar um número
    try:
        opcao_in = int(input("Digite 1 para perímetro ou 2 para área: "))        
        if opcao_in == 1: # Adicionado :
            ladoA_in = float(input("Lado A: "))
            ladoB_in = float(input("Lado B: "))
            ladoC_in = float(input("Lado C: "))
            perimetro_do_triangulo(ladoA_in, ladoB_in, ladoC_in)            
        elif opcao_in == 2: # Usar elif ou else com :
            base_in = float(input("Base: "))
            altura_in = float(input("Altura: "))
            # Removido o : do final da chamada da função
            area_do_triangulo(base_in, altura_in)
        else:
            print("Opção inválida!")            
    except ValueError:
        print("Erro: Digite apenas números válidos.")

if __name__ == "__main__":
    main()