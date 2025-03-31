def unicode_range(text: str) -> dict:
    """ Возращает словарь символов, символ юникод - целое число"""
    a, b = [int(i) for i in text.split()]
    return {chr(i): i for i in range(a, b+1)}

if __name__ == '__main__':
    text = input("Ведите два числа: ")
    print(unicode_range(text))