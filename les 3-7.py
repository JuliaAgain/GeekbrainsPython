#вводят строку. сотсавить словарь ключ - символ. знаечние - его количество
from collections import Counter
str_user = input("Введите строку: ")
dic = {}
for letter in str_user:
    dic[letter] = str_user.count(letter)
print(Counter(str_user))
print(dic)