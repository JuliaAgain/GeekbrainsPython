""""Напишите функцию для транспонирования матрицы."""


def transpon_matrix(matrix: list) -> list: #на вход подается матрицы размером m*n
    m = len(matrix) #число строк в исходной матрице
    n = len(matrix[0]) #число столбцов в исходной матрице
    new_matrix = [0]*n #создаем новую матрицу, в которой n строк и m столбцов
    for i in range(n):
        new_matrix[i] = [0]*m #заполянем новую матрицу нулями, получается матрица размером n*m
    for i in range(n): #пробегаемся циклами по элементам новой матрицы и заменяем каждый ноль нужнм элементов исходной матрицы
        for j in range(m):
            new_matrix[i][j] = matrix[j][i]

    return new_matrix

if __name__ == '__main__':
    matrix1 = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    matrix2 = [[0, 2],
               [3, 5],
               [7, 9],
               [1, 2]]
    for row in transpon_matrix(matrix1):
        print(*row)
        print()
    for row in transpon_matrix(matrix2):
        print(*row)
