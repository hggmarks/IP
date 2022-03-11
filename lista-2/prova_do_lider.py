letra = input()
numero = int(input()) 

if letra == 'X' and numero % 2 == 1:
    for i in range(numero):
        for j in range(numero):
            if j == 0+i or j == numero-i-1:
                print('X', end='')
            else:
                print('0', end='')
        if i != numero-1:
            print(end="\n\n")
        else:
            print()
elif letra == 'T' and numero % 2 == 1:

    for i in range(numero):
        for j in range(numero):
            if i == 0 or j == int(numero/2):
                print('X', end='')
            else:
                print('0', end='')
        if i != numero-1:
            print(end="\n\n")
        else:
            print()
elif letra == 'O' and numero % 2 == 1:
    
    for i in range(numero):
        for j in range(numero):
            if i == 0 or i == numero-1 or j == 0 or j == numero-1:
                print('X', end='')
            else:
                print('0', end='')
        if i != numero-1:
            print(end="\n\n")
        else:
            print()
else:
    print('Entrada não permitida')
