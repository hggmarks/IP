from itertools import count


def get_five_cards():
    i = 5
    cards = []
    while i > 0:
        nome, poder = input().split('/')
        cards.append([nome, int(poder)]) 
        i-= 1
    return cards

if __name__ == '__main__':
    counter = 0
    luke_cards = get_five_cards()
    inscryption_cards = get_five_cards()
    luke_wins = False
    inscryption_wins = False
    luke_ganhou = False
    alguem_ganhou = False
    while counter < 5 and not alguem_ganhou:
        if luke_cards[counter][1] > inscryption_cards[counter][1]:
            print(f'Luke foi muito esperto, usou {luke_cards[counter][0]} e ganhou o {counter+1}º round!')
            luke_wins += 1
        else:
            print(f'Inscryption nao aliviou, usou {inscryption_cards[counter][0]} e venceu o {counter+1}º round!')
            inscryption_wins += 1
        
        if luke_wins == 3 or inscryption_wins == 3:
            alguem_ganhou = True
        
        counter += 1
        
    if luke_wins > inscryption_wins:
        print(f'Luke Carter ganhou na batalha de cartas e avançou de fase na sua luta para conseguir sair da cabana!')
    else:
        print(f'Luke Carter foi derrotado na batalha de cartas e sua alma permanecera na cabana para todo o sempre!')
            
