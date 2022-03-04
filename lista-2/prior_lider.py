letra_sorteada = input()
num_participantes = int(input())
nome_vencedor = ''
palavra_vencedor = ''
quantidade_letra_vencedor = 0
quantidade_letra = 0

while num_participantes > 0:
    nome, palavra = input().split('-')

    for letra in palavra:

        if letra == letra_sorteada:
            quantidade_letra += 1

    if quantidade_letra > quantidade_letra_vencedor:
        quantidade_letra_vencedor = quantidade_letra
        nome_vencedor = nome
        palavra_vencedor = palavra

    num_participantes -= 1
    quantidade_letra = 0


if nome_vencedor == 'Prior':
    print(
        f'Joga y joga! Mago Prior e o novo lider com a palavra {palavra_vencedor} com {quantidade_letra_vencedor} aparicoes da letra {letra_sorteada}.')
else:
    print(
        f'Vish! O Mago Prior pode ir pro paredao, ja que quem ganhou foi {nome_vencedor}, com a palavra {palavra_vencedor} e {quantidade_letra_vencedor} aparicoes da letra {letra_sorteada}.')
