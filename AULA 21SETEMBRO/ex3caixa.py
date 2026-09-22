class ContaBancaria:

    def __init__(self, nome_titular, saldo=0):
        self.nome_titular = nome_titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("Erro: Valor inválido.")

    def _debitar(self, valor):
        self.__saldo -= valor

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: Valor inválido.")

        elif valor <= self.__saldo:
            self._debitar(valor)
            print("Saque realizado com sucesso!")

        else:
            print("Erro: Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Titular: {self.nome_titular}")
        print(f"Saldo: R$ {self.__saldo:.2f}")


class ContaEspecial(ContaBancaria):

    def __init__(self, nome_titular, saldo=0, limite=0):
        super().__init__(nome_titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: Valor inválido.")

        elif valor <= self.saldo + self.limite:
            self._debitar(valor)
            print("Saque realizado com sucesso!")

        else:
            print("Erro: Saldo e limite insuficientes.")


# ==========================================
# PROGRAMA PRINCIPAL - CAIXA ELETRÔNICO
# ==========================================

print("================================")
print("       CAIXA ELETRÔNICO")
print("================================")

nome = input("Digite o nome do titular: ")
limite = float(input("Digite o limite da conta: R$ "))

# Criando uma instância de ContaEspecial
conta = ContaEspecial(nome, 0, limite)


# Menu interativo
while True:

    print("\n========= MENU =========")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("0 - Sair")
    print("========================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        valor = float(input("Digite o valor do depósito: R$ "))
        conta.depositar(valor)

    elif opcao == "2":

        valor = float(input("Digite o valor do saque: R$ "))
        conta.sacar(valor)

    elif opcao == "3":

        conta.consultar_saldo()
        print(f"Limite: R$ {conta.limite:.2f}")
        print(f"Total disponível: R$ {conta.saldo + conta.limite:.2f}")

    elif opcao == "0":

        print("Caixa eletrônico encerrado.")
        break

    else:

        print("Opção inválida. Tente novamente.")


