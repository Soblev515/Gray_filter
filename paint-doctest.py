import math

def circle_area(radius):
    """
    Return circle area
    :param radius: radius circle
    :return: circle area -> double
    >>> circle_area(5)
    78.53981633974483
    >>> circle_area(3)
    28.274333882308138
    """
    return math.pi * float(radius) * float(radius)

def rectangle_area(width, height):
    """
    Return rectangle area
    :param width: width rectangle
    :param height: height rectangle
    :return: rectangle area -> double
    >>> rectangle_area(5, 2)
    10
    >>> rectangle_area(20, 3)
    60
    """
    return width * height


def square_area(side):
    """
    Return square area
    :param side: side square
    :return: square area -> double
    >>> square_area(5)
    25
    >>> square_area(1)
    1
    """
    return side * side


def degree_to_rad(angle):
    """
    Return radian from degree
    :param angle: angle in degree
    :return: angle in red -> double
    >>> degree_to_rad(5)
    0.08726646259971647
    >>> degree_to_rad(30)
    0.5235987755982988
    """
    return angle * math.pi / 180


def parallelogram_area(base, side, angle_degree):
    """
    Return parallelogram area
    :param base: base parallelogram
    :param side: side parallelogram
    :param angle_degree: angle parallelogram in degree
    :return: angle in red -> double
    >>> parallelogram_area(5, 2, 90)
    10.0
    >>> parallelogram_area(30, 1, 8)
    4.175193028801963
    """
    return base * side * math.sin(degree_to_rad(angle_degree))


def triangle_area(a, b, angle_degree):
    """
    Return triangle area
    :param a: first side triangle
    :param b: second side triangle
    :param angle_degree: angle from first and second side in degree
    :return: triangle area -> double
    >>> triangle_area(5, 2, 30)
    2.4999999999999996
    >>> triangle_area(30, 1, 8)
    2.0875965144009814
    """
    return 0.5 * parallelogram_area(a, b, angle_degree)


def parse_args(string: str):
    """
    Parse arguments
    :param string: n-arguments
    :return: figure, area_args, volume
    >>> parse_args("Круг, 3, 1")
    ('Круг', [3], 1)
    >>> parse_args("Прямоугольник, 4 5, 9")
    ('Прямоугольник', [4, 5], 9)
    """
    string_args = string.split(', ')
    return string_args[0], [int(i) for i in string_args[1].split()], int(string_args[2])


def area_factory(figure, *args):
    """
    Return figure area
    :param figure: name figure
    :param *args: list arguments figure
    :return: area figure
    >>> area_factory("Круг", 3)
    28.274333882308138
    >>> area_factory("Прямоугольник", 4, 5)
    20
    >>> area_factory("Квадрат", 5)
    25
    >>> area_factory("Треугольник", 6, 2, 10)
    1.041889066001582
    >>> area_factory("Параллелограмм", 5, 3, 10)
    2.6047226650039548
    """
    if figure == 'Круг':
        return circle_area(*args)
    if figure == 'Прямоугольник':
        return rectangle_area(*args)
    if figure == 'Квадрат':
        return square_area(*args)
    if figure == 'Треугольник':
        return triangle_area(*args)
    if figure == 'Параллелограмм':
        return parallelogram_area(*args)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
