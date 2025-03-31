"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
 Если ключ не хешируем, используйте его строковое представление."""


def change_keys_values(**kwargs) -> dict:
    """Принимает словарь и возвращает словарь, где менет места клюи и значения """
    result = {} #создаем новый пустой словарь, который будем заполнять в цикле
    for k, v in kwargs.items():
        try:
            hash(v) #проверяем хешируемо ли значение
        except:
            v = str(v) #если не хешируемо, берем строковое представление значения
        result[v] = k
    return result

if __name__ == '__main__':
    print(change_keys_values(name = 'Tina', height = 185, age = 26))
    print(change_keys_values(company='MS', budget=185_000_000, legal = True))
    print(change_keys_values(group = 'students', num = 5, results = [4, 5, 2, 4, 4]))