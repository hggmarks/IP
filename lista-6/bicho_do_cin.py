lista_animais_ord = ['avestruz', 'aguia', 'burro', 'borboleta', 'cachorro', 'cabra', 'carneiro', 'camelo', 'cobra', 'coelho', 'cavalo', 'elefante', 'galo', 'gato', 'jacare', 'leao', 'macaco', 'porco', 'pavao', 'peru', 'touro', 'tigre', 'urso', 'veado', 'vaca']


def fill_dict(animais: list):
    contador_index_lista = 0
    valor_animal = 1
    lista_valores = []
    dezenas_bixos = {}
    while contador_index_lista < len(animais):
        lista_valores.append("0"+str(valor_animal)) if valor_animal < 10 else lista_valores.append(str(valor_animal))
        valor_animal += 1
        if valor_animal % 4 == 1:
            new_key_value = {animais[contador_index_lista]: lista_valores}
            dezenas_bixos.update(new_key_value)
            contador_index_lista += 1
            lista_valores = []

    dezenas_bixos[animais[-1]][3] = '00'

    return dezenas_bixos


if __name__ == '__main__':
    dezenas_bixos = fill_dict(lista_animais_ord)
