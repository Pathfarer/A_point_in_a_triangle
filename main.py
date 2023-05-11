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


def square_triangle(x1, y1, x2, y2, x3, y3):  # функция рассчета площади треугольника
    def lenght(a1, b1, a2, b2):  # функция рассчета длины отрезка по двум координатам
        return ((a1 - a2) ** 2 + (b1 - b2) ** 2) ** 0.5  # находим длину по теореме Пифагора

    # Высчитываем длины сторон треугольника:
    lenght_a = lenght(x1, y1, x2, y2)
    lenght_b = lenght(x1, y1, x3, y3)
    lenght_c = lenght(x2, y2, x3, y3)
    # Высчитываем полупериметр треугольника:
    half_perimeter = (lenght_a + lenght_b + lenght_c) / 2
    # Высчитываем площадь треугольника по формуле Герона, используя посчитанные ранее длины треугольника и полупериметр:
    return (half_perimeter * (half_perimeter - lenght_a) * (half_perimeter - lenght_b) * (
            half_perimeter - lenght_c)) ** 0.5


square = square_triangle(coor_x1, coor_y1, coor_x2, coor_y2, coor_x3, coor_y3)  # Площадь основного треугольника
square1 = square_triangle(user_x, user_y, coor_x1, coor_y1, coor_x2, coor_y2)  # Площади треугольника,
square2 = square_triangle(user_x, user_y, coor_x1, coor_y1, coor_x3, coor_y3)  # образованные заданной точкой
square3 = square_triangle(user_x, user_y, coor_x2, coor_y2, coor_x3, coor_y3)  # и двумя вершинами треугольника
# Если точка внутри треугольника, то сложив площади трех треугольников, образованных этой точкой и двумя вершинами
# треугольника, получим площадь изначального треугольника:
if (square1 + square2 + square3) == square:
    print('Точка внутри треугольника')
else:
    print('Точка снаружи треугольника')
print(f'{square} = {square1} + {square2} + {square3}')
