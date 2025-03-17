import fractions
from fractions import Fraction
while True:
    s1 = input("Введите дробь вида 'a/b': ")
    s2 = input("Введите дробь вида 'a/b': ")
    if not isinstance(s1, str) or not isinstance(s2, str):
        print("Ошибка типа данных. Введите строку.")
    elif '/' not in s1 or '/' not in s2:
        print('Попробуйте еще раз.')
    else:
        break
def shorten(x, y): # функция для сокращения дроби с числителем числителем и знаменателем
    divids = []  #в этот пустой список добавим все общие делителм числителя и заменателя и найдем из них максимальный
    for i  in range(2, x+1):
        if x%i ==0 and y%i == 0:
            divids.append(i)
    if len(divids) > 0:
        m = max(divids)
        x = int(x/m)
        y = int(y/m)

    return str(x)+'/'+str(y)


n1 = fractions.Fraction(s1)
n2 = fractions.Fraction(s2)
a1, b1 = [int(i) for i in s1.split('/')] #ищем числители и знаменатели дробей
a2, b2 = [int(i) for i in s2.split('/')]
product_a = a1*a2 #перемножаем числители дробей
product_b = b1*b2 #перемножаем знаменатели дробей
print(f"Произведение дробей: {shorten(product_a, product_b)}")
sum_a = a1*b2 + a2*b1 #ищем числитель дроби, которая равна сумме введенных дробей
sum_b = b1*b2
print(f"Сумма дробей: {shorten(sum_a, sum_b)}")
print(f"Проверка. Произведение дробей: {n1*n2}. Сумма дробей: {n1+n2}.")




