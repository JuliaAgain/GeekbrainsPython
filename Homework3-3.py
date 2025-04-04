#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.
things = {"палатка": 5000, #словарь со значениями массы вещей в граммах
          "чашка": 200,
          "термос": 800,
          "спальник": 1200,
          "спички": 50,
          "котелок": 500,
          "тушенка": 300}

m = int(input("Введите максимальную грузоподъемность рюкзака в граммах: "))
things_list = list(things.keys()) #это спикоск всех вещей в рюкзаке
for i in range(len(things_list)): #будем пробешать по списку вещей и заполнять рюкзак, каждый раз начиная с с разного слова в списке
    backpack_weight = 0 #каждый раз обнуляем массу рюкзака
    backpack = []        #каждый раз создаем пустой список вещей рюкзака, кладем туда вещи по условию
    for j in range(len(things_list)-i):
        s = things_list[i+j] #s -  вещь, с которой мы начинаем заполнять рюкзак, в каждом цикле разная
        if (things[s] + backpack_weight) <= m:
            backpack_weight += things[s]
            backpack.append(s)
    print(f"В рюкзак можно поместить эти вещи: {backpack}. Масса рюкзака составит: {backpack_weight} грамм.")

