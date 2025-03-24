#создать словарь имя друга- кортеж вещей
dic_things = {
    "Юра": ("котелок", "палатка", "рюкзак"),
    "Сергей": ("рюкзак", "палатка", "спички", "лопата"),
    "Олег": ("стол", "рюкзак", "продукты")
    }
first = list(dic_things.keys())[0]
res = set(dic_things[first])
for k, v in dic_things.items():
    res = res.intersection(set(v))
print("У все есть ", *res)

dic_count = {}
for k, v in dic_things.items():
    for i in v:
        dic_count[i] = dic_count.get(i, 0) + 1
friends = len(list(dic_things.keys())) - 1
print(dic_count)
things = []

for k, v in dic_count.items():
    if v == friends:
        things.append(k)
for k, v in dic_things.items():
    for t in things:
        if t not in v:
            print(f"{t} нет у {k}")
            break
singles = []
for k, v in dic_count.items():
    if v ==1:
        singles.append(k)
print(*singles, "есть только у 1 человека")


