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
        operacao = input()
        if (operacao in libero) or (operacao in levantador) or (operacao in central) or (operacao in ponteiro) or (operacao in oposto):
            if operacao == 'Samuel':
                print('Sim, Samuel, voce ja esta na lista de jogadores')
            else:
                print(f'Sim, {operacao} esta na lista de jogadores')
        else:
            if operacao == 'Samuel':
                print('Como voce pode esquecer de si mesmo? Voce nao esta na lista')
            else:
                print(f'O jogador {operacao} nao esta na lista de jogadores')
        
    elif entrada == 'nomes': 
        operacao = input()
        if operacao == 'Libero':
            if libero != []:
                print('Os liberos sao:')
                print(*libero, sep='\n')
            else: 
                print('Ainda nao temos jogadores nessa posicao')
        elif operacao == 'Levantador':
            if levantador != []:
                print('Os levantadores sao:')
                print(*levantador, sep='\n')
            else:
                print('Ainda nao temos jogadores nessa posicao')
        elif operacao == 'Central':
            if central != []:
                print('Os centrais sao:')
                print(*central, sep='\n')
            else:  
                print('Ainda nao temos jogadores nessa posicao')
        elif operacao == 'Ponteiro':
            if ponteiro != []:
                print('Os ponteiros sao:')
                print(*ponteiro, sep='\n')
            else:
                print('Ainda nao temos jogadores nessa posicao')
        elif operacao == 'Oposto':
            if  oposto != []:
                print('Os opostos sao:')
                print(*oposto, sep='\n')
            else:
                print('Ainda nao temos jogadores nessa posicao')
    else:
        print('***COMANDO INVALIDO***')
        

if(len(libero) == 2 and len(libero)+len(levantador)+len(ponteiro)+len(central)+len(oposto) <= 18):
    print(f'O Navegantes esta pronto para disputar o Estadual! Desejem sorte aos nossos {len(libero)+len(levantador)+len(ponteiro)+len(central)+len(oposto)} jogadores!')
else:
    print('Quem mandou ficar perdendo tempo com TikTok... Agora o Navegantes nao conseguira jogar o estadual :(')
