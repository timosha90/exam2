#Написать программу для вывода уникальных значений из списка словарей

list_1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
a = set()
for i in list_1:
    for j in i.values():
        a.add(j)
print(a)
