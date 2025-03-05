import decimal
import math
decimal.getcontext().prec = 50
d = decimal.Decimal(input("Введите диаметр до 1000: "))
if d > 1000:
    print("Слишком большое число")
r = d/2
pi = decimal.Decimal(math.pi)
s = pi*r**2
length = 2*pi*r
print(s, length)
print(len(str(s)), len(str(length)))