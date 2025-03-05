from decimal import Decimal
MIN_SUM = 50
PROCENT_COMISSION = 0.015
MIN_COMISSION = 30
MAX_COMISSION = 600
BONUS = 0.03
LIMIT_BEFORE_TAX = 5_000_000
TAX_RATE = 0.1
def menu(balance: Decimal, count: int, is_flag: bool):
    dct = {1: "Пополнить счет",
           2: "Снять со счета",
           3: "Выйти из программы"}
    print("Добро пожаловать в программу Банкомат.")
    print("Выберите команду: ")
    for k, v in dict.items():
        print(f"{k}: {v}")
    if balance > LIMIT_BEFORE_TAX:
        balance*=(1 - TAX_RATE)
    choice = int(input())
    if choice == 3:
        print(balance)
        return balance, is_flag
    elif choice ==1:
        balance = give_money(balance)
        count+=1
    elif choice ==2:
        balance = get_money(balance)
        count+=1
    else:
        print("Неверная команда")
    if count % 3 ==0:
        balance+=(1+BONUS)
    print(balance)
    return balance, is_flag

def get_money(balance: Decimal):
    money_to_get = Decimal(input("Введите сумму снятия: "))
    procent = money_to_get * PROCENT_COMISSION

    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMISSION:
            procent = MIN_COMISSION
        elif procent > MAX_COMISSION:
            procent = MAX_COMISSION

        if money_to_get + procent >= balance:
            return balance - (money_to_get + procent)
        else:
            print("Недостаточно средств для сниятия")
            return balance

def give_money():
    pass