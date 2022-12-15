#1 Написать программу для получения списка словарей из списков.

color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
colours = list(dict(color_name for color_name in color_code))
print(colours)
colours = list(dict(zip(color_name, color_code)))


color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

b = []
for i, j in zip(color_name, color_code):
    b.append({'color_name': i, 'color_code': j})
print(b

