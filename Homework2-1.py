#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
BASE =16
dct = {10: 'A', 11: 'B', 12: 'C', 13: "D", 14: 'E', 15: 'F'}
num = int(input("Введите целое число: "))
print(hex(num))
result = ''
while num >= BASE: #ищем остатки от деления, по очереди добвляем их к строке
    digit = num % BASE
    if digit >9:
        symbol = dct[digit]
    else:
        symbol = str(digit)
    result+=symbol
    num //= BASE
result+= str(num)
print(result[::-1]) #переворачиваем строку


