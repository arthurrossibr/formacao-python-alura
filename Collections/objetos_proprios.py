class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


def deposita_para_todas(lista_de_contas):
    for c in lista_de_contas:
        c.deposita(100)


conta_teste = ContaCorrente(200)
conta_teste2 = ContaCorrente(250)
conta_teste.deposita(500)
conta_teste2.deposita(5000)

contas = [conta_teste, conta_teste2]
for conta in contas:
    print(conta)

deposita_para_todas(contas)
for conta in contas:
    print(conta)

tupla = ('Arthur', 21, 2000)
tupla2 = ('Paula', 30, 1991)

# def deposita(conta): # variação "funcional" (separando o comportamento dos dados)
#   novo_saldo = conta[1] + 100
#     codigo = conta[0]
#     return codigo, novo_saldo

usuarios = [tupla, tupla2]
print(usuarios)

conta_teste3 = ContaCorrente(15)
conta_teste3.deposita(1000)
contas_t = (conta_teste3, conta_teste2)
for conta in contas_t:
    print(conta)

contas_t[0].deposita(500)
for conta in contas_t:
    print(conta)
