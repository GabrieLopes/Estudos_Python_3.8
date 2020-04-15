print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentiva {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite seu número: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o numero secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o numero secreto.")

    rodada = rodada + 1

print("Fim do jogo")