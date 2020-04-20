import random


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")


def inserir_palavras_secretas():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def chute_do_jogador():
    chute = input("Qual letra?").strip().upper()
    return chute


def chute_jogador_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("Você ganhou!!")


def imprime_mensagem_perdedor():
    print("Você perdeu!!")


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = inserir_palavras_secretas()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    # enquanto(True)
    while (not enforcou and not acertou):

        chute = chute_do_jogador()

        if (chute in palavra_secreta):
            chute_jogador_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()


if (__name__ == "__main__"):
    jogar()
