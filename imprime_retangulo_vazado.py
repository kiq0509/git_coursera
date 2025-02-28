largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

matriz = ''
simbolo = '#'

linha = ''
a = 0
l = 0

for a in range(altura):
        linha = ''
        for l in range(largura):
            if a == 0 or a == altura-1 or l == 0 or l == largura-1:
                simbolo = '#'
            else:
                simbolo = ' '

            linha += simbolo

        matriz += f'{linha}\n'
print(matriz)