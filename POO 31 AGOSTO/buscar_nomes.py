nomes=["Adonis","Andressa","Beatriz"]


busca=input("Qual nome deseja buscar? ").title()

if busca in nomes:
    print(f"Sim, {busca} está na lista")

else:
    print(f"Nao, {busca} nao foi encontrado")