# Есть файл text.txt. Вывести слово, имеющее минимальную длину. Обработать исключения.

try:
    f =open("text.txt", "r").read().split()
    lm = 2
    for w in f:
        l = len(w)
        if l < lm:
            print(w)
except FileNotFoundError:
    print('Файл не найден')








