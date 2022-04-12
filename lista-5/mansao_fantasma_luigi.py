from typing import Union

def bin_search(sorted_list: list, term: Union[str, int], low: int, high: int, index_offset: int = 0) -> tuple:

    if low <= high:
        mid = (low + high) // 2
        
        if term == sorted_list[mid]:
            return mid+index_offset, sorted_list[mid]
        
        elif term > sorted_list[mid]:
            return bin_search(sorted_list, term, mid+1, high, index_offset)
        
            
        return bin_search(sorted_list, term, low, mid-1, index_offset)
        
    else:
        return (-1, -1)


def get_capicua(num: int) -> int:
    stringified_num = str(num)
    reversed_num = int(stringified_num[::-1])
    if stringified_num == stringified_num[::-1]:
        return num
    else:
        return get_capicua(num + reversed_num)

if __name__ == '__main__':
        WEAPOW_NAME = 'Ghost Potrificationizer - E. Gadd'
        books = []
        num_inputs = int(input()) 
        counter = num_inputs

        while counter > 0:
            books.append(input())
            counter -= 1

        low = 0
        high = len(books)-1
        weapow_index, weapow_name = bin_search(books, WEAPOW_NAME, low, high, 1)

        if weapow_index == -1:
            print('Mamma mia! Só Mario poderá me salvar agora!')

        else:
            weapow_power = weapow_index*7
            weapow_power = get_capicua(weapow_power)

            if weapow_power < 50:
                print('É uma catástrofe, eu tenho a arma mas só posso usá-la uma vez')
            elif weapow_power < 100:
                print('Terei que usar a minha arma com sabedoria!')
            elif weapow_power < 200:
                print('A arma está bem carregada, me dei bem!')
            else:
                print('Aha! EU NÃO TENHO MAIS MEDO DE NADA! PODEM VIR!')