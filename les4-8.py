"""Создайте несколько переменных, заканчивающихся на s.
Напишите функцию, которая при запуске меняет содержимое переменных, заканчивающихся на s?
кроме одной s на None/
Значения не удаляются, а помещатся в одноименные значения без s  на конце."""

def no_s():
    """Удаляет s из имен переменных."""
    lst = {}
    for k, v in globals().items():
        if k != 's' and k != 'no_s' and k.endswith('s'):
            lst[k[:-1]] = v
            globals()[k] = None
    for k, v in lst.items():
        globals()[k] = v

if __name__ == '__main__':
    items = 0
    names = 'jdsjksjks'
    s = 5
    value = 'fgfg'
    print(globals())
    no_s()
    print(globals())

