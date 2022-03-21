entrada = ''
operacao = []
libero = []
levantador = []
central = []
ponteiro = []
oposto = []

while entrada != 'fim':
    entrada = input()

    if entrada == 'adicionar':
        #adicionando jogador a sua posição
        operacao = input().split(': ')
        
        if operacao[1] == 'Libero':
            libero.append(operacao[0])
        elif operacao[1] == 'Levantador':
            levantador.append(operacao[0])
        elif operacao[1] == 'Central':
            central.append(operacao[0])
        elif operacao[1] == 'Ponteiro':
            ponteiro.append(operacao[0])
        elif operacao[1] == 'Oposto':
            oposto.append(operacao[0])
        

        #verificando quantidade de liberos
        if len(libero) > 2:
            print('ERRO: liberos demais, nao temos uniformes suficientes')
            break
        
        #verificando mais de 5 jogadores por posição
        if len(levantador) == 5:
            print('Cuidado! voce ja possui 5 levantadores')
        if len(central) == 5:
            print('Cuidado! voce ja possui 5 centrais')
        if len(ponteiro) == 5:
            print('Cuidado! voce ja possui 5 ponteiros')
        if len(oposto) == 5:
            print('Cuidado! voce ja possui 5 opostos')
        
        if (len(levantador) + len(central) + len(ponteiro) + len(oposto) + len(libero)) > 18:
            print('ERRO: voce estrapolou o numero de jogadores')
            break
    
    elif entrada == 'relatorio':
        total = len(libero)+len(levantador)+len(ponteiro)+len(central)+len(oposto)
        print('No nosso time ja possuimos:')
        print(f'Liberos: {len(libero)}')
        print(f'Levantadores: {len(levantador)}')
        print(f'Ponteiros: {len(ponteiro)}')
        print(f'Centrais: {len(central)}')
        print(f'Opostos: {len(oposto)}')
        print(f'TOTAL: {total}')
    elif entrada == 'buscar':
        
    elif entrada == 'nomes': 
        operacao = input()
        if operacao == 'libero':
            if libero != []:
                print(f'Os liberos são:')
                print(*libero, sep='\n')
            else: 
                print('Ainda nao temos jogadores nessa posicao')