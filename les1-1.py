n = int(input("Введите число:"))
e = int(input("e:"))
count = 2
sum_1 = 0
while count <=n:
    if count % e ==0:
        count+=2
        continue
    sum_1 += count
    count+=2
print(sum_1)