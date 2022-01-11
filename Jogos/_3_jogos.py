import _1_adivinhacao
import _2_forca


def escolhe_jogo():
    print("*********************************")
    print("Escolha seu jogo!")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        print("Jogando forca")
        _2_forca.jogar()
    elif jogo == 2:
        _1_adivinhacao.jogar()
        print("Jogando adivinhação")


if __name__ == "__main__":
    escolhe_jogo()
