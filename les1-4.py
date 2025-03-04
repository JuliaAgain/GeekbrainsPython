#наривовать елку из *, спросив количество рядов
rows  =  int(input("Введите число рядов для елки:"))
for i in range(1, rows+1):
    spaces = rows -i
    stars = 2*i - 1
    print(" "* spaces + '*' * stars)
