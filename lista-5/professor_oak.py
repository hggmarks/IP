def mdc(num_a: int, num_b: int) -> int:
    if num_b == 0:
        return num_a
    else:
        return mdc(num_b, num_a % num_b)


if __name__ == '__main__':
    pokebolas = int(input())
    pocoes = int(input())
    revives = int(input())

    mdc_pokebolas_pocoes = mdc(pokebolas, pocoes)
    mdc_final = mdc(mdc_pokebolas_pocoes, revives)

    if mdc_final > 1:
        print(f'Gracas a Companhia Pokemon, {mdc_final} treinadores pokemon vao receber itens do Professor!')

    else:
        print('Infelizmente apenas 1 treinador pokemon ira receber os itens hoje, e com certeza nao e o atrasado do Ash.')
