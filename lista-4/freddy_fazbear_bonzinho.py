
def is_palindromo(text: str):
    if text.replace(' ', '').lower() == text.replace(' ', '')[::-1].lower():
        return True
    else:
        return False

def is_pangrama(text: str, alphabet: tuple):
    letter_counter = 0
    for letter_alpha in alphabet:
        first_appearance = False
        for letter_text in text.replace(' ', '').lower():
            if letter_text == letter_alpha and not first_appearance:
                letter_counter += 1
                first_appearance = True
    
    if letter_counter == len(alphabet):
        return True
    else:
        return False

def is_epizeuxis(text: str):
    words = text.split()
    i = 0
    while i < len(words):
        if i < len(words)-1 :
            if words[i] == words[i+1]:
                return True
        i += 1
    return False
        

if __name__ == '__main__':
    alfabeto = ('a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','x','z')

    num_entradas = int(input())

    while num_entradas > 0:
        frase = input()
        if is_palindromo(frase):
            print(f'Freddy, "{frase}" é um palíndromo!')
        elif is_pangrama(frase, alfabeto):
            print(f'Tenho certeza de que "{frase}" é um pangrama!')
        elif is_epizeuxis(frase):
            print(f'Freddy, Freddy, "{frase}" é definitivamente uma epizeuxe!')
        else:
            print('Essa aqui é uma pegadinha, não há nada aqui!')


        num_entradas -= 1
