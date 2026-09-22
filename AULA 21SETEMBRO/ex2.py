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
        else:
            print("Erro: Valor inválido")

    def _debitar(self, valor):
        self.__saldo -= valor

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: Valor inválido")

        elif valor <= self.__saldo:
            self._debitar(valor)

        else:
            print("Erro: Saldo Insuficiente")

    def consultar_saldo(self):
        print(f"Titular: {self.nome_titular}")
        print(f"Saldo: R$ {self.__saldo:.2f}")


class ContaEspecial(ContaBancaria):

    def __init__(self, nome_titular, saldo=0, limite=0):
        super().__init__(nome_titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: Valor inválido")

        elif valor <= self.saldo + self.limite:
            self._debitar(valor)

        else:
            print("Erro: Saldo e limite insuficientes")