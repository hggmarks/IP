fim_lista = False
comando = ''
convidados = []
while not fim_lista:
    entrada = input()
    if entrada == 'adicionar':

        comando = input().split()
        nome, index = comando
        convidados.insert(int(index), nome)

    elif entrada == 'remover':

        comando = input()
        convidados.remove(comando)

    elif entrada == 'atualizar indice':

        comando = input().split()
        nome, index = comando
        nome_antigo = convidados[int(index)]
        convidados_buffer = convidados.copy()
        posicao_antiga = convidados.index(nome)
        convidados[int(index)] = nome
        convidados[posicao_antiga] = nome_antigo
        
        if convidados == convidados_buffer:
            print('Nada mudou, a lista permanece igual')
            
    elif entrada == 'imprimir lista atual':

        for convidado in convidados:
            if convidado != convidados[len(convidados)-1]:
                print(f'{convidado} ', end='')
            else:
                print(f'{convidado}')

    elif entrada == 'lista finalizada':
       fim_lista = True
    else:
        print('Opçao não encontrada')
    
else:
    print('A lista ficou da seguinte forma:')
    for convidado in convidados:
            if convidado != convidados[len(convidados)-1]:
                print(f'{convidado} ', end='')
            else:
                print(f'{convidado}')

