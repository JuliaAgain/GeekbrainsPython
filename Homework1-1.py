#Треугольник существует только тогда, когда сумма любых двух его
# сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить
# является ли треугольник разносторонним, равнобедренным или равносторонним.

a, b, c = list(map(float, input("Введите длины трех сторон треугольника через пробел: ").split()))
if c > (a+b) or b > (a+c) or a > (b+c):
    print("Треугольника с такими сторонами не существует.")
elif a==c==b:
    print("Это равносторонний треугольник.")
elif (a**2 + b**2) == c**2 or (a**2+c**2) == b**2 or (c**2 + b**2) == a**2:
    print("Это прямоугольный треугольник.")
else:
    print("Это разносторонний теругольник.")
