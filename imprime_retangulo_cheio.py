largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

cont_l = 0
cont_a = 0

while cont_l <= largura:
    print('#',end= ' ')
    while cont_a <= altura:
        cont_a+=1
        print('#',end= ' ')
    cont_l+=1
    print()
        
        