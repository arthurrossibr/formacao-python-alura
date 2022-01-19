# idade1 = 39
# idade2 = 30
# idade3 = 27
# idade4 = 18
#
# print(idade1)
# print(idade2)
# print(idade3)
# print(idade4)

idades = [39, 30, 27, 18]
print(len(idades))
print(idades[1])
print(idades[3])

idades.append(15)
print(idades)

for idade in idades:
    print(idade)

idades.remove(15)
print(idades)

idades.append(15)
idades.append(15)
print(idades)

idades.remove(15)
print(idades)

# idades.clear()
# print(idades)

# ----------------------------

print(15 in idades)

if 15 in idades:
    idades.remove(15)
    print(idades)

idades.insert(0, 20)
print(idades)

idades.sort()
print(idades)

idades.extend([40, 52, 36])
print(idades)

idades_nova = []
for idade in idades:
    idades_nova.append(idade + 1)
print(idades_nova)

idades_nova2 = [(idade + 1) for idade in idades]
print(idades_nova2)

teste = [idade for idade in idades if idade > 21]
print(teste)


def processa_visualizacao(lista=None):
    if lista is None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)


# ----------------------------

idades = [15, 87, 65, 56, 32, 49, 37]

for idade in idades:
    print(idade)

print(list(enumerate(idades)))

for indice, idade in enumerate(idades):
    print(indice, idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios:  # ja desempacotando
    print(nome)

for nome, _, _ in usuarios:  # ja desempacotando, ignorando o resto
    print(nome)

# ----------------------------

ordenado = sorted(idades)
print(ordenado)

reverso = reversed(idades)
print(reverso)

unico = list(reversed(sorted(idades)))
unico2 = sorted(idades, reverse=True)
print(unico)
print(unico2)
