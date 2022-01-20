usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

print(assistiram)
print(len(assistiram))
print(set(assistiram))
print({1, 2, 3, 1})
print(type({1, 2}))

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_machine_learning)

# print(usuarios_machine_learning[3]) não funciona

for usuario in set(assistiram):
    print(usuario)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_data_science | usuarios_machine_learning)
print(usuarios_data_science & usuarios_machine_learning)
print(usuarios_data_science - usuarios_machine_learning)

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning

print(15 in fez_ds_mas_nao_fez_ml)
print(23 in fez_ds_mas_nao_fez_ml)
print(usuarios_data_science ^ usuarios_machine_learning)

usuarios = {1, 5, 76, 34, 52, 13, 17}
print(len(usuarios))

usuarios.add(28)
print(usuarios)

new_usuarios = frozenset(usuarios)  # nn permite mudar

meu_texto = "Bem vindo texto para teste de texto para fazer teste"
meu_texto = set(meu_texto.split())
print(meu_texto)
