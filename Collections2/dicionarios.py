# Dicionário -----------

aparicoes = {"Guilherme": 1, "cachorro": 2, "nome": 2, "vindo": 1, "Carlos": 2}

del aparicoes["Carlos"]
print(aparicoes)
print("cachorro" in aparicoes)
print("Carlos" in aparicoes)

for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento, aparicoes[elemento])

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, "=", valor)

print(["palavra {}".format(chave) for chave in aparicoes.keys()])

# ----------------------------
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)

from collections import Counter

aparicoes = Counter(meu_texto.split())

print(aparicoes)