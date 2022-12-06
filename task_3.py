# Дан списко кортежей. Написать программу, которая меняет последнее значение элемента кортежей.

list_1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
list_1[0] = list(list_1[0])
list_1[1] = list(list_1[1])
list_1[2] = list(list_1[2])
print(list_1)
list_1[0][2] = int(input('Введите число '))
list_1[1][2] = int(input('Введите число '))
list_1[2][2] = int(input('Введите число '))

list_1[0] = tuple(list_1[0])
list_1[1] = tuple(list_1[1])
list_1[2] = tuple(list_1[2])
print(list_1)


