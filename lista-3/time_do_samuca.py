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
        if len(levantador) > 5:
            print('Cuidado! voce ja possui 5 levantadores')
        if len(central) > 5:
            print('Cuidado! voce ja possui 5 centrais')
        if len(ponteiro) > 5:
            print('Cuidado! voce ja possui 5 ponteiros')
        if len(oposto) > 5:
            print('Cuidado! voce ja possui 5 opostos')
        
        if (len(levantador) + len(central) + len(ponteiro) + len(oposto) + len(libero)) > 18:
            print('ERRO: voce estrapolou o numero de jogadores')
            break
    
    elif entrada == 'relatorio':
        print('No nosso time ja possuimos:')
        print(f'Liberos: {len(libero)}')
        print(f'Levantadores: {len(levantador)}')
        
    elif entrada == 'nomes':
    elif entrada == 'buscar':