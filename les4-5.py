"""Функция принимает на вход три списка одинаковой дины:
именна str, ставка int, премия стр у казанием процента.
Вернуть словарь с где имя - ключ, значение - сумма премии. сумма = стака*процент"""


def calculate_bonus(names: list[str], rates: list[int], percents: list[str]) -> dict:
    """Возввращает премии."""
    calculation = {}
    for name, rate, percent in zip(names, rates, percents):
        percent = float(percent[:-1])
        calculation[name] = rate * percent/100
    return calculation


if __name__ == '__main__':
    names = ['Kim', 'Kendal', 'Kloe']
    rates = [60000, 80_000, 85_000]
    percents = ['10.25%', '5.00%', '9.10%']
    print(calculate_bonus(names, rates, percents))
