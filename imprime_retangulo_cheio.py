largura = int(input('digite a largura: ')) -1
altura = int(input('digite a altura: '))

cont_l = 0
cont_a = 0

while cont_a < altura:
    print('#',end= '')
    while cont_l < largura:
        cont_l+=1
        print('#',end= '')
    cont_l = 0
    cont_a+=1
    print()
        
        
