#вводят строку. вывести каждое слово с ной строки
text_lst = input("Введите строку: ").split()
text_lst.sort()
max_len = max([len(word) for word in text_lst])
max_len1 = len(max(text_lst, key = len))
for i, word in enumerate(text_lst, 1):
    print(f'{i} {word: >{max_len}}')
