#Создатьь вручную список, удалить элементы, которые встречаются дважды
from collections import Counter
lst = [1, 2, 1, 1, 5, 6, 5, 9, 10, 9]
dic2 = Counter(lst)
dic = {}
for i in lst:
    if i not in dic:
        dic[i] = 0
    dic[i] +=1
for k, v in dic.items():
    if v ==2:
        lst.remove(k)
        lst.remove(k)
print(lst)
print(dic2)
print(dic)