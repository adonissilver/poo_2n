

def validar_triangulo(a,b,c):

    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False



def tipo_triangulo(a,b,c):
    if a==b and b==c:
        return "Equilatero"
    if (a==b) or (a==c) or (b==c): 
        return "Isosceles"
    else:
        return "Escaleno"



def main():
    print("Validador de triangulo")

    try:
        a=float(input("Digite o comprimento do primeiro lado: "))
        b=float(input("Digite o segundo lado: "))
        c=float(input("Digite o terceiro lado: "))

        if validar_triangulo(a,b,c):
            print("Os lados formam um triangulo válido")

            tipo=tipo_triangulo(a,b,c)
            print(tipo)
        else:
            print("Triangulo nao válido")
    except:
        print("Vc digitou um valor inválido")



if __name__ == "__main__":
    main()        