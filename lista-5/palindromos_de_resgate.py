def is_palindrome(word: str) -> bool:
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

def is_palindrome_with_a(word: str) -> str:
    if not (is_palindrome(word)):      
        if word.endswith('a'):
            return is_palindrome_with_a(word[:-1])
        else:
            return is_palindrome(word)
    else:
        return True
        
if __name__ == '__main__':
    num_pistas = int(input())
    contador = num_pistas
    num_acertos = 0
    while contador > 0:
        pista = input()
        if is_palindrome_with_a(pista):
            num_acertos += 1
        contador -= 1
    if num_acertos != num_pistas:
        print('Essa não!!! Estou na direção errada.')
    else:
        print('ACHEI!!! Peach, estou a caminho.')
