def demonstrar_strings(frase):
    # Texto de exemplo com espaços propositais no início e fim
    
    print(f"Frase original: '{frase}'")
    print("-" * 40)

    # 1. len() - Tamanho da string
    print(f"1. Tamanho total (com espaços): {len(frase)}")

    # 2. strip() - Remove espaços em branco do início e do fim
    frase_limpa = frase.strip()
    print(f"2. Sem espaços extras: '{frase_limpa}'")

    # 3. lower() e upper() - Minúsculas e Maiúsculas
    print(f"3. Tudo em minúsculo: {frase_limpa.lower()}")
    print(f"4. Tudo em maiúsculo: {frase_limpa.upper()}")

    # 4. capitalize() e title() - Formatações de início
    exemplo = "engenharia de software"
    print(f"5. Capitalize (Só a 1ª letra da frase): {exemplo.capitalize()}")
    print(f"6. Title (1ª letra de cada palavra): {exemplo.title()}")

    # 5. replace() - Substitui um trecho por outro
    nova_frase = frase_limpa.replace("INCRÍVEL", "Poderosa")
    print(f"7. Substituindo palavra: {nova_frase}")

    # 6. split() - Divide a frase em uma lista de palavras
    palavras = frase_limpa.split()
    print(f"8. Lista de palavras: {palavras}")

    # 7. join() - Une elementos de uma lista em uma string
    unido = "-".join(palavras)
    print(f"9. Palavras unidas por hífen: {unido}")

    # 8. Buscas: find() e count()
    print(f"10. Posição da palavra 'linguagem': {frase_limpa.find('linguagem')}")
    print(f"11. Quantas vezes aparece a letra 'a': {frase_limpa.count('a')}")

    # 9. Verificações: startswith() e isdigit()
    print(f"12. Começa com 'Python'? {frase_limpa.startswith('Python')}")
    
    numero = "12345"
    print(f"13. O texto '{numero}' é numérico? {numero.isdigit()}")

if __name__ == "__main__":
    frase_in = input("Digite uma frase: ") 
    demonstrar_strings(frase_in)