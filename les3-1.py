lst = [1, 2, 3, 1, 2]

print(list(set(lst)))
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)