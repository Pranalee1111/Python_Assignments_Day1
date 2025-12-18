
def get_even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

if __name__ == '__main__':
    print(get_even_numbers([1, 2, 3, 4, 5, 6]))
