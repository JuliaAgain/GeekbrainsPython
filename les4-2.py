def text_unicode(text: str) -> list:
    """Функция принимает строку и формирует список с уникальными кодами юникод каждого символа"""
    return list(map(ord, sorted(set(text), reverse = True)))

if __name__ == '__main__':
    print(text_unicode(input("введите строку: ")))
