num_eliminados = int(input())
contador = num_eliminados
emparedado = ''
ganhador = ''
while contador > 0:

    pessoa_que_saiu = input()

    if emparedado == '': emparedado = pessoa_que_saiu

    if pessoa_que_saiu == 'Prior':
        print('IIIHHH! El mago esta eliminado!')
    elif pessoa_que_saiu == 'Manu':
        print('Manu saiu! Bruna Marquezine deve estar muito triste :(')
    elif pessoa_que_saiu == 'Pyong':
        print('Agora o Pyong que dormiu, esta eliminado')
    elif pessoa_que_saiu == 'Gizelly':
        print('PPPPPYYYYYOOOONNNGGG LEEEEEE, Gizelly volta pra casa!')

    if num_eliminados == 19 and contador == 1:
        ganhador = pessoa_que_saiu
    contador -= 1

print(f'- O indicado(a) ao paredao nessa semana e: {emparedado}')

if num_eliminados != 19:
    print(f'- Ainda restam {19 - num_eliminados} pessoas na disputa pela lideranca!')
else:
    print(f'- O novo lider da semana e: {ganhador}!')
