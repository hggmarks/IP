entrada = input()
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
        convidados_buffer = convidados.copy()
        convidados[int(index)], convidados[convidados.index(nome)] = convidados[convidados.index(nome)], convidados[int(index())]

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

