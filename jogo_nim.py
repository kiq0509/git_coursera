def computador_escolhe_jogada(n, m):
    # Se o número de peças é menor ou igual ao máximo permitido, retira todas.
    if n <= m:
        return n
    # Se for possível deixar múltiplos de (m+1), essa é a jogada ideal.
    resto = n % (m + 1)
    if resto > 0:
        return resto
    # Caso contrário, retira o máximo possível.
    return m


def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada < 1 or jogada > m or jogada > n:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            return jogada


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    # Define quem inicia a partida
    if n % (m + 1) == 0:
        print("Você começa!")
        usuario_turn = True
    else:
        print("Computador começa!")
        usuario_turn = False

    while n > 0:
        if usuario_turn:
            jogada = usuario_escolhe_jogada(n, m)
            if jogada == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou {} peças.".format(jogada))
        else:
            jogada = computador_escolhe_jogada(n, m)
            if jogada == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou {} peças.".format(jogada))
        n -= jogada

        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        elif n > 0:
            print("Agora restam {} peças no tabuleiro.".format(n))
        usuario_turn = not usuario_turn

    if usuario_turn:
        print("Fim do jogo! O computador ganhou!")
        return "computador"
    else:
        print("Fim do jogo! Você ganhou!")
        return "usuario"


def campeonato():
    placar_usuario = 0
    placar_computador = 0
    for rodada in range(1, 4):
        print("\n**** Rodada {} ****".format(rodada))
        vencedor = partida()
        if vencedor == "computador":
            placar_computador += 1
        else:
            placar_usuario += 1
    print("\n**** Final do campeonato! ****")
    print("Placar: Você {} X {} Computador".format(placar_usuario, placar_computador))


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    opcao = int(input())
    if opcao == 1:
        print("\nVocê escolheu uma partida isolada!")
        partida()
    elif opcao == 2:
        print("\nVoce escolheu um campeonato!")
        campeonato()



main()
