BASE = 8
number = int(input("Введите число: "))
result = ''
while number >= BASE:
    result += str(number % BASE)
    number //= BASE
result+=str(number)
print(result[::-1])
print(oct(number))
