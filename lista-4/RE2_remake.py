def espacos_sobrando(total: int, ocupados:int):
    return total-ocupados

def gerador_qtd_inputs(counter: int):
    i = 0
    while i < counter:
        item, quantidade = input().split(' - ')
        yield item, quantidade
        i+=1


def espacos_sobrando_atuais(total: int, ocupados:int, novas_pochetes: int):
    return espacos_sobrando(total, ocupados)+2*novas_pochetes

if __name__ == '__main__':
    slots_totais = int(input())
    slots_ocupados = int(input())
    itens_qtd = [(item, quantidade) for item, quantidade in gerador_qtd_inputs(slots_ocupados)]
    pochetes = int(input())
    print(f'Voce possui {slots_totais} slots no inventario e {slots_ocupados} estao ocupados.')
    print(f'Espacos sobrando [{espacos_sobrando(slots_totais, slots_ocupados)}]')

    print()

    if(slots_ocupados == 0):
        print('Seu inventário ainda está vazio. Que sorte... ou azar. Tome cuidado.')
    else:    
        print('Lista de itens:')
        for item in itens_qtd:
            print(f'{item[0]} [{item[1]}]')
    print()
    if pochetes == 0:
        print('Você ainda não encontrou pochetes. Seus espaços continuam os mesmos.')
    else:

        print(f'Voce conseguiu {pochetes} pochete(s) e agora possui {espacos_sobrando_atuais(slots_totais, slots_ocupados, pochetes)+slots_ocupados} slots de inventario.')
        print(f'Espacos sobrando [{espacos_sobrando_atuais(slots_totais, slots_ocupados, pochetes)}]')

