# Размерность матрицы вводится с клавиатуры, заполнить матрицу случайными числами от 10 до 50.
# Найти наибольшую сумму элементов в столбцах матрицы. Вывести индекс столбца с максимальной суммой элементов на экран
from random import randint
M = int(input("Введите количество строк "))
N = int(input("Введите количество столбцов "))
A = [[randint(10, 50) for i in range(M)] for j in range(N)]
for j in range(N):
    print(A[j])
a = 0
b = 0
for i in range(M):
    sum1 = 0
    for j in range(N):
        sum1 += A[j][i]
    if sum1 > a:
        a = sum1
        b = i
print(f'Наибольшая сумма{a}, столбец {b}')


