data = input("Введите данные: ")

if data.isdecimal():
    print(f"{int(data)} целое число.")
else:
    try:
        print(f"{float(data)} - вещественное число.")
    except ValueError:
        if data.lower() != data:
            print(data.lower())
        else:
            print(data.upper())
