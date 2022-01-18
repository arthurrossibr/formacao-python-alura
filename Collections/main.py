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
    idades_nova.append(idade+1)
print(idades_nova)

idades_nova2 = [(idade + 1) for idade in idades]
print(idades_nova2)

teste = [idade for idade in idades if idade > 21]
print(teste)
