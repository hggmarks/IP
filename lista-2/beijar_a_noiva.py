local_mapa = int(input())

entrada_progresso = int(input())
progresso = 0
soma = 0

while entrada_progresso > 0:
    progresso = entrada_progresso
    while progresso > 0:
        soma += progresso
        progresso -= 1
    entrada_progresso = int(input())

if soma < local_mapa:
    print('Ainda nos falta um pouco...')
elif soma == local_mapa:
    print('Pode beijar a noiva, afinal, vocês conseguiram!')
elif soma < 20*local_mapa:
    print('Parece que os pombinhos passaram um pouco do local...')
elif soma < 100*local_mapa:
    print('Acho que nos perdemos um pouco no caminho, onde estamos?')
else:
    print('Hum... acho que o casal deve rever seus votos de matrimônio...')
