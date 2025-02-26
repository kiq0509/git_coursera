import random
def computador_escolhe_jogada(n,m):
    escolha = 1
    print('O computador tirou uma peça.')
    # fazer m +1
    if m+1 % n == 0:
        escolha = m - ((m+1)/n)
    else:
        escolha = m

    if escolha > n:
        escolha = n

    if escolha == 1:
        print('O computador tirou uma peça.')
    if escolha > 1:
        print(f'O computador tirou {escolha} peças.')
    return escolha

def usuario_escolhe_jogada(n,m):
    escolha = int(input('Quantas peças você vai tirar?'))
    while escolha <= 0 or escolha > n or escolha > m:
        print('Oops! Jogada inválida! Tente de novo.')
        escolha = int(input('Quantas peças você vai tirar?')) 
    return escolha

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    comeca = random.randrange(1,3)

    if comeca == 1:
        print("computador")

    else:
        print('mano')