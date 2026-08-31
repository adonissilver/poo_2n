def somar(a, b):
    return a + b

# Se não tivesse o 'if __name__', isso rodaria SEMPRE, 
# mesmo se você só quisesse importar a função somar em outro lugar.
if __name__ == "__main__":
    print("Testando a soma:", somar(5, 5))



    x=float(input("Digite o primeiro número: "))    
    y=float(input("Digite o segundo número: "))


    print("Testando a soma:", somar(x, y))