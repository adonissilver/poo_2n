#exercicio 1

class ContaBancaria:
    def __init__ (self,nome_titular,saldo=0):
        self.nome_titular=nome_titular
        self.saldo=saldo

    def depositar(self,valor):
        self.saldo=self.saldo+valor

    def sacar(self,valor):
        if valor<=self.saldo:
            self.saldo-=valor
        else:
            print("Erro: Saldo Insuficiente")

    def  consultar_saldo(self):
        print(f"Titular: {self.nome_titular}")
        print(f"Saldo: R$ {self.saldo:.2f}")

    
    