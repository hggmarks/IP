
relacionamentos = [[-1,  5,  5,  5,  5,  5,  5],
                  [ 5, -1,  6,  5,  5,  5,  5],
                  [ 5,  6, -1,  5,  5,  5,  5],
                  [ 5,  5,  5, -1,  7,  4,  5],
                  [ 5,  5,  5,  7, -1,  3,  4],
                  [ 5,  5,  5,  4,  3, -1,  7],
                  [ 5,  5,  5,  5,  4,  7, -1]]

nomes = ['sam', 'chris', 'ashley', 'jessica', 'mike', 'emily', 'matt']

def alterar_relacionamento(relacionamentos_tab: list, num_relacionamentos: int):
    while num_relacionamentos > 0:
        nome_1, tipo_interacao, nome_2 = input.split(' ')
        if tipo_interacao == 'X':
            relacionamentos_tab[nomes.index(nome_1)][nomes.index(nome_2)] -= 1
        else:
            relacionamentos_tab[nomes.index(nome_1)][nomes.index(nome_2)] += 1

        num_relacionamentos -=1
    return relacionamentos_tab
