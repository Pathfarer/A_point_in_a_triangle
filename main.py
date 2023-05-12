import random  # Импорт рандомайзера

# Задаем случайные координаты вершин треугольника:
coor_x1 = random.randint(-5, 5)
coor_x2 = random.randint(-5, 5)
coor_x3 = random.randint(-5, 5)
coor_y1 = random.randint(-5, 5)
coor_y2 = random.randint(-5, 5)
coor_y3 = random.randint(-5, 5)
# Выводим случайные координаты на экран:
print(f'Координаты треугольника: {coor_x1};{coor_y1}  {coor_x2};{coor_y2}  {coor_x3};{coor_y3}')
# Вносим координаты точки, которую будем рассматривать относительно треугольника:
user_x, user_y = map(int, input('Введите координаты точки через пробел: ').split())


# Решение через площади. Имеются искажения.

# def square_triangle(x1, y1, x2, y2, x3, y3):  # функция рассчета площади треугольника
#     def lenght(a1, b1, a2, b2):  # функция рассчета длины отрезка по двум координатам
#         return ((a1 - a2) ** 2 + (b1 - b2) ** 2) ** 0.5  # находим длину по теореме Пифагора
#
#     # Высчитываем длины сторон треугольника:
#     lenght_a = lenght(x1, y1, x2, y2)
#     lenght_b = lenght(x1, y1, x3, y3)
#     lenght_c = lenght(x2, y2, x3, y3)
#     # Высчитываем полупериметр треугольника:
#     half_perimeter = (lenght_a + lenght_b + lenght_c) / 2
#     # Высчитываем площадь треугольника по формуле Герона, используя посчитанные ранее длины треугольника и
#     полупериметр:
#     return (half_perimeter * (half_perimeter - lenght_a) * (half_perimeter - lenght_b) * (
#             half_perimeter - lenght_c)) ** 0.5
#
#
# square = square_triangle(coor_x1, coor_y1, coor_x2, coor_y2, coor_x3, coor_y3)  # Площадь основного треугольника
# square1 = square_triangle(user_x, user_y, coor_x1, coor_y1, coor_x2, coor_y2)  # Площади треугольника,
# square2 = square_triangle(user_x, user_y, coor_x1, coor_y1, coor_x3, coor_y3)  # образованные заданной точкой
# square3 = square_triangle(user_x, user_y, coor_x2, coor_y2, coor_x3, coor_y3)  # и двумя вершинами треугольника
# # Если точка внутри треугольника, то сложив площади трех треугольников, образованных этой точкой и двумя вершинами
# # треугольника, получим площадь изначального треугольника:
# if (square1 + square2 + square3) == square:
#     print('Точка внутри треугольника')
# else:
#     print('Точка снаружи треугольника')
# print(f'{square} = {square1} + {square2} + {square3}')

# Решение через векторное и псевдоскалярное произведение.
def point_in_triangle(x1, y1, x2, y2, x3, y3, x0, y0):
    a = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
    b = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
    c = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
    if a == 0 or b == 0 or c == 0:
        return print('Точка лежит на стороне треугольника')
    elif (a < 0 and b < 0 and c < 0) or (a > 0 and b > 0 and c > 0):
        return print('Точка внутри треугольника')
    else:
        return print('Точка снаружи треугольника')


point_in_triangle(coor_x1, coor_y1, coor_x2, coor_y2, coor_x3, coor_y3, user_x, user_y)
