tup = (12, 'ffff', 'fikmc', 26.13, 1522, 'fjfjf')
dic_type = {}
for i in tup:
    t = type(i).__name__
    if t not in dic_type:
        dic_type[t] = []
    dic_type[t].append(i)
print(dic_type)