from operator import attrgetter
from functools import total_ordering


@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def __eq__(self, other):
        if type(other != ContaSalario) and not isinstance(other, ContaSalario):
            return False
        return self._codigo == other._codigo

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


conta1 = ContaSalario(10)
print(conta1)

conta2 = ContaSalario(10)
print(conta2)
print(conta1 == conta2)

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in contas:
    print(conta)

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

print(conta_do_guilherme > conta_da_daniela)

for conta in sorted(contas):
    print(conta)

print(conta_do_guilherme <= conta_da_daniela)
