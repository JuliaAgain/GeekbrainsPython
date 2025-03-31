"""список числе - сортировка пузырьком"""

def sort_numbers(num_list: list) -> None:
    """сортирует числа на месте без sorted"""
    for _ in range(len(num_list)):
        for j in range(len(num_list)-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

if __name__ == '__main__':
    lst = [int(i) for i in input("Ведите список чисел: ").split()]
    sort_numbers(lst)
    print(lst)