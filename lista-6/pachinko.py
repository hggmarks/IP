tabela_de_registros = {
    'bichinho de pelucia': {
        'quantidade': 10,
        'preco': 750,
        'resgatados': 0
    },
    'boneco articulado com armadura': {
        'quantidade': 20,
        'preco': 1000,
        'resgatados': 0
    },
    'estatua de cena memoravel': {
        'quantidade': 10,
        'preco': 1250,
        'resgatados': 0
    },
    'camiseta tematica': {
        'quantidade': 10,
        'preco': 500,
        'resgatados': 0
    },
    'chaveiro': {
        'quantidade': 50,
        'preco': 250,
        'resgatados': 0
    },
    'bolinhas': {
        'quantidade': 10000,
        'quantidade_recebida': 0,
        'preco': 1000,
        'resgatados': 0
    }
}

def comprar(tabela_de_registros: dict, num_bolinhas_vendidas: int) -> dict:
    preco_bolinhas = tabela_de_registros['bolinhas']['preco']
    if tabela_de_registros['bolinhas']['quantidade'] >= num_bolinhas_vendidas:
        tabela_de_registros['bolinhas']['quantidade'] -= num_bolinhas_vendidas
        tabela_de_registros['bolinhas']['resgatados'] += 1
        print(f'O jogador comprou {num_bolinhas_vendidas} bolinhas por {num_bolinhas_vendidas*preco_bolinhas} ienes.')
    else:
        print(f'Nao ha mais bolinhas disponiveis, melhor esperar um pouco.')    
    
    return tabela_de_registros

def trocar(tabela_de_registros: dict, premio: str, bolinhas: int) -> dict:
    try: 
        if tabela_de_registros[premio]['quantidade'] >= 0:
            if tabela_de_registros[premio]['preco'] <= bolinhas:

                tabela_de_registros[premio]['quantidade'] -= 1
                tabela_de_registros[premio]['resgatados'] += 1
                tabela_de_registros['bolinhas']['quantidade_recebida'] += tabela_de_registros[premio]["preco"]

                print(f'O jogador trocou {tabela_de_registros[premio]["preco"]} bolinhas por um {premio}.')
            else:
                print(f'O jogador precisa de mais {tabela_de_registros[premio]["preco"]-bolinhas} bolinhas para trocar por um {premio}.')
        else:
            print(f'O jogador veio trocar suas bolinhas mas o premio {premio} nao esta disponivel.')
    except KeyError:
        print(f'O jogador veio trocar suas bolinhas mas o premio {premio} nao esta disponivel.')

    return tabela_de_registros

def relatorio(tabela_de_registros: dict):
    print()
    premios_restantes = 0
    bolinhas_recebidas = 0
    resgates = 0

    for premio in tabela_de_registros:
        if premio != 'bolinhas':
            premios_restantes += tabela_de_registros[premio]['quantidade']
            bolinhas_recebidas += tabela_de_registros[premio]['resgatados']*tabela_de_registros[premio]['preco']
            resgates += tabela_de_registros[premio]['resgatados']

    print('O resumo do dia foi:')
    print(f'Arrecadado: {(10000 - tabela_de_registros["bolinhas"]["quantidade"])*tabela_de_registros["bolinhas"]["preco"]} ienes em {tabela_de_registros["bolinhas"]["resgatados"]} vendas;')
    print(f'Bolinhas: {tabela_de_registros["bolinhas"]["quantidade"]+tabela_de_registros["bolinhas"]["quantidade_recebida"]} restantes;')
    print(f'Resgates feitos: {resgates};')
    print(f'Bolinhas recebidas: {bolinhas_recebidas};')
    print(f'Premios: {premios_restantes} restantes;')
    print('Deu a hora, amanha tem mais!')


if __name__ == '__main__':
    comando = ''

    while comando != 'hora de fechar':
        comando = input()

        if comando == 'comprar':
            num_bolinhas_vendidas = int(input())
            tabela_de_registros = comprar(tabela_de_registros, num_bolinhas_vendidas)
        elif comando == 'trocar':
            entrada = input().split(' - ')
            premio, qtd_bolinhas = entrada[0], int(entrada[1])

            tabela_de_registros = trocar(tabela_de_registros, premio, qtd_bolinhas)
    else:
        relatorio(tabela_de_registros)


