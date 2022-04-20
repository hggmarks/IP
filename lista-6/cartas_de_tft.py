cards_values = {item[0]:item[1] for i in range(5) for item in [input().split(' - ')]}

ordered_cards = {key: value for key, value in sorted(cards_values.items(), key=lambda chave_valor: chave_valor[1])}

for key in ordered_cards:
    print(f'{key} - {ordered_cards[key]}')
