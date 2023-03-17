# Определяем класс для точек
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Определяем класс для треугольников
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Функция, которая вычисляет площадь треугольника
    def area(self):
        return abs((self.b.x - self.a.x) * (self.c.y - self.a.y) - (self.c.x - self.a.x) * (self.b.y - self.a.y)) / 2


# Цикл по всем файлам входных данных (input1.txt, input2.txt и т.д.)
for i in range(1, 6):
    input_file = f"input{i}.txt"
    output_file = f"output{i}.txt"

    # Считываем данные из файла inputN.txt
    triangles = []
    with open(input_file) as f:
        for line in f:
            coords = list(map(int, line.strip().split()))
            a = Point(coords[0], coords[1])
            b = Point(coords[2], coords[3])
            c = Point(coords[4], coords[5])
            triangle = Triangle(a, b, c)
            triangles.append(triangle)

    # Сортируем треугольники по площади
    triangles.sort(key=lambda t: t.area())

    # Записываем отсортированные треугольники в файл outputN.txt
    with open(output_file, 'w') as f:
        for triangle in triangles:
            f.write(f"{triangle.a.x} {triangle.a.y} {triangle.b.x} {triangle.b.y} {triangle.c.x} {triangle.c.y}\n")
