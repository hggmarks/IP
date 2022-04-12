from typing import Union

def bin_search(sorted_list: list, term: Union[str, int], low: int, high: int) -> tuple:

    if low <= high:
        mid = (low + high) // 2
        
        if term == sorted_list[mid]:
            return mid, sorted_list[mid]
        
        elif term > sorted_list[mid]:
            return bin_search(sorted_list, term, mid+1, high)
        
            
        return bin_search(sorted_list, term, low, mid-1)
        
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
        weapow_index, weapow_name = bin_search(books, WEAPOW_NAME, low, high)
        weapow_power = weapow_index*7
        weapow_power = get_capicua(weapow_power)

        
        



arr = [3,7,9,11,14,19,24,29,39]

element = 49

a = bin_search(arr, element, low, high)

print(a)


#if __name__ == '__main__':
#    WEAPOW_NAME = 'Ghost Potrificationizer - E. Gadd'
#    num_inputs = int(input()) 
#    counter = num_inputs
#    weapow_index = 0
#    while counter > 0:
#        name = input()
#        if name = WEAPOW_NAME:
#            weapow_index = num_inputs - counter
#
#        counter -= 1
#
#    weapow_power = weapow_index*7

