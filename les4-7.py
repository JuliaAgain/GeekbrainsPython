"""Функция получает соварь с компанией в качестве ключа.
Знаечние список с доходами и расходами.
Вычислить итоговую прибыль компании. Если всек омпании прибыльныеБ
вернуть истину, если нет - ложь."""


def all_profitable(profits: dict) -> bool:
    """Подсчет убыточности."""
    lst = [sum(value)>0 for value in profits.values()]
    return all(lst)

if __name__ == '__main__':
    profits = {'Hp': [100, -200, 500, -10],
               'Zoom': [0, 89, -10, 60, -780],
               'Ms': [89, 56, -10]}
    print(all_profitable(profits))