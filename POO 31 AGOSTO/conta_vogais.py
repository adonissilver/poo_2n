def contavogais(frase):
    vogais= "aeiou"
    contador=0

    for letra in frase:
        if letra in vogais:
            contador+=1
            print(f"Encontrada a vogal: {letra}")
    return contador




def main():
    frase=input("Digite uma frase: \n")
    frase=frase.lower()
    contador=contavogais(frase)
    print(f"A frase contém {contador} vogais.")

if __name__== "__main__":
    main()
