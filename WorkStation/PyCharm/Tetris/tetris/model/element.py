"""代表俄罗斯方块元素，包括砖块"""
import unittest


# Point
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __str__(self):
        return "[x:" + str(self.x) + ", y:" + str(self.y) + "]"


class Brick:
    """砖块"""
    def __init__(self, point):
        if not isinstance(point, Point):
            raise ValueError("Value must be instance of namedtuple")
        self.point = point

    def move_down(self):
        """砖块向下"""
        self.point.y += 1

    def move_up(self):
        self.point.y -= 1

    def move_left(self):
        self.point.x -= 1

    def move_right(self):
        self.point.x += 1

    def __str__(self):
        return self.point.__str__()


class Element:

    def __init__(self):
        self.__bricks = []

    @property
    def bricks(self):
        return self.__bricks

    @bricks.setter
    def bricks(self, bricks):
        if not isinstance(bricks, list):
            raise ValueError("Bricks must be instance of list")
        self.__bricks = bricks

    def move_down(self):
        """向下"""
        for b in self.__bricks:
            b.move_down()

    def move_left(self):
        """向左"""
        for b in self.__bricks:
            b.move_left()

    def move_up(self):
        """向上"""
        for b in self.__bricks:
            b.move_up()

    def move_right(self):
        for b in self.__bricks:
            b.move_right()

    def __iter__(self):
        return self.__bricks.__iter__()


class Element1(Element):

    def __init__(self):
        pass # TODO


# test
class TestBrick(unittest.TestCase):

    def setUp(self):
        self.brick = Brick(Point(1, 2))

    def test_init(self):
        b = self.brick
        self.assertEqual(b.point, Point(1, 2))
        self.assertTrue(isinstance(b, Brick))

    def test_move_down(self):
        b = Brick(Point(1, 2))
        b.move_down()
        self.assertEqual(b.point, Point(1, 3))


class TestElement(unittest.TestCase):

    def test_setter(self):
        e = Element()
        bricks = [Brick(Point(1, 2)), Brick(Point(1, 3))]
        e.bricks = bricks
        self.assertEqual(e.bricks, bricks)

    def test_iter(self):
        e = Element()
        bricks = [Brick(Point(1, 2)), Brick(Point(1, 3))]
        e.bricks = bricks
        for b in e.bricks:
            print(b)
