# проверка на високосность

year = int(input("Введите год после 1582: "))
IGNORE =  1582
if year < IGNORE:
    print("Слишком ранний год.")
else:
    if year % 4 ==0 and (year % 400 == 0 or year % 100 !=0):
        print("Это високосный год")
    else:
        print("Это не обычный год")