"""Создать генератор простых чисел."""

def prime(n):
    if n<3:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

def generate_simple(m):
    for i in range(2, m):
        if i > 200:
            raise StopIteration
        if prime(i):
            yield i

g = generate_simple(int(input("Введите число N: ")))
for i in g:
    print(i, end = " ")
