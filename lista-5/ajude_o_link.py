def check_primality(num_a: int, num_b = 2):

    if num_a <= num_b:
        return True if num_a == 2 else False
    elif num_a % num_b == 0:
        return False
    elif num_b ** 2 > num_a:
        return True

    return check_primality(num_a, num_b + 1)

def check_digit_sum(number: int)->int:

    if number//10 == 0:
        return number
    return number%10 + check_digit_sum(number//10)

def digit_sum_is_even(number):
    num = check_digit_sum(number)
    if num % 2 == 0:
        return [True, num]
    return [False, num]

def factorial(number: int) -> int:

    if number == 1:
        return 1
    return number * factorial(number -1)

def factorial_number_guesser(number: int, predicition: int) -> bool:
    if factorial(number) == predicition:
        return True
    return False

if __name__ == '__main__':
    won = 0
    lost = 0

    while won < 3 and lost < 3:

        caminho = input()


        if caminho == 'Somar':
            number = int(input())
            result, result_sum = digit_sum_is_even(number)
            if result:
                print(f'O número {result_sum} é par, siga por aqui Link!')
                won += 1
                lost = 0
    
            else:
                print('Por aqui não.')
                lost += 1
                won = 0
        elif caminho == 'Primo':
            number = int(input())
            result = check_primality(number)
            if result:
                print(f'O número {number} é primo, continue herói!')
                won += 1
                lost = 0
            else:
                print('Por aqui não.')
                lost += 1
                won = 0
        elif caminho == 'Fatorial':
            data = input().split()
            number = int(data[0])
            predicition = int(data[1])
            result = factorial_number_guesser(number, predicition)

            if result:
                print(f'A resposta é mesmo {data[1]} Link, esse caminho está certo!')
                won += 1
                lost = 0
            else:          
                print('Por aqui não.')
                lost += 1
                won = 0
        else:
            print('Por aqui não.')
            lost += 1
            won = 0
    else:
        if won == 3:
            print('Com a sua ajuda o Link finalmente conseguiu sair do labirinto!!!')
        elif lost == 3:
            print('Hoje não é um bom dia para o nosso herói...')
            

