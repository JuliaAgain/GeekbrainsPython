"""Функция принимает список чисел и два индекс.
Вернуть сумму числе между этими индексами"""


def sum_range(numbers: list, x1: int, x2: int) -> int:
    """Возвращает сумму между индексами включительно."""
    if x1 > x2:
        x1, x2 = x2, x1
    if x1<0:
        x1 = 0
    if x2 >= len(numbers):
        x2 = len(numbers) - 1
    return sum(numbers[x1: x2+1])


if __name__ == '__main__':
    numbers = [3, 5, 7, 67, 100]
    x1 = 1
    x2 = 4
    print(sum_range(numbers, x1, x2))