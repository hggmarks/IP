def increase_speed(initial_speed: int, num_coins: int, race_way: str) -> int:
    bonus : int = 0
    if(race_way == 'Mario Kart Stadium'):
        bonus = 3
    elif (race_way == 'Bowsers Castle'):
        bonus = 4
    elif (race_way == 'Moo Moo Meadows'):
        bonus = 5
    elif (race_way == 'Yoshi Valley'):
        bonus = 6
    elif (race_way == 'Rainbow Road'):
        bonus = 7
    
    if num_coins == 1:
        return bonus + initial_speed 
    else:
        new_speed : int = initial_speed + bonus
        return increase_speed(new_speed, num_coins-1, race_way)

if __name__ == '__main__':
    competidor : str = input()
    velocidade_inicial : int = int(input())
    nome_da_pista : str = input()
    quantidade_moedas : int = int(input())

    velocidade_final = increase_speed(velocidade_inicial, quantidade_moedas, 
                                        nome_da_pista)
    
    print(f'Correndo na pista {nome_da_pista}, {competidor} coletou {quantidade_moedas} moedas e terminou a corrida na incrivel velocidade de {velocidade_final} km/h.')
