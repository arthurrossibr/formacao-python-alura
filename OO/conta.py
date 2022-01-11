class __Conta:

    def __init__(self, agencia, numero, titular, saldo, limite):
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de R${} do titular".format(self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saque(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor R${}, ultrapassou seu limite".format(valor))

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigo_dos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
