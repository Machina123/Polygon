import math
from abc import ABC, abstractmethod
from params import Length, Colour, Ratio, Angle, MathHelpers
from gui import GUI

class ConvexPolygon(ABC):

    fill_colour = Colour(name="Fill colour")
    outline_colour = Colour(name="Outline colour")

    @abstractmethod
    def __init__(self):
        self.fill_colour = "white"
        self.outline_colour = "black"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self, scale=1):
        pass

    def set_fill_colour(self, colour):
        self.fill_colour = colour

    def set_outline_colour(self, colour):
        self.outline_colour = colour

class Triangle(ConvexPolygon):
    len_base = Length(name="Length of base")
    len_height = Length(name="Height of triangle")
    ratio_h_div = Ratio(name="Ratio of base intersection with height")

    def __init__(self, len_base, len_height, ratio_h_div):
        super().__init__()
        self.len_base = len_base
        self.len_height = len_height
        self.ratio_h_div = ratio_h_div

    def area(self):
        return self.len_base * self.len_height * 0.5

    def perimeter(self):
        side_b = math.sqrt(((self.len_base * self.ratio_h_div) ** 2) + (self.len_height ** 2))
        side_c = math.sqrt(((self.len_base * (1 - self.ratio_h_div)) ** 2) + (self.len_height ** 2))
        return self.len_base + side_b + side_c

    def draw(self, scale=1):
        scaled_base = self.len_base * scale
        scaled_height = self.len_height * scale
        coords = [(0, 0), (scaled_base, 0), (self.ratio_h_div * scaled_base, scaled_height)]
        GUI.draw_polygon(self, coords, self.fill_colour, self.outline_colour, scale)
        pass

class ConvexQuadrilateral(ConvexPolygon):
    len_diag1 = Length(name="Length of first diagonal")
    len_diag2 = Length(name="Length of second diagonal")
    ratio_intersect_diag1 = Ratio(name="Ratio of diagonals intersection (for 1st diag.)")
    ratio_intersect_diag2 = Ratio(name="Ratio of diagonals intersection (for 2nd diag.)")
    angle_btwn_diagonals = Angle(name="Angle between diagonals")

    def __init__(self, len_diag1, len_diag2, ratio_intersect_diag1, ratio_intersect_diag2, angle_btwn_diagonals):
        super().__init__()
        self.len_diag1 = len_diag1
        self.len_diag2 = len_diag2
        self.ratio_intersect_diag1 = ratio_intersect_diag1
        self.ratio_intersect_diag2 = ratio_intersect_diag2
        self.angle_btwn_diagonals = angle_btwn_diagonals

    def area(self):
        return 0.5 * self.len_diag1 * self.len_diag2 * math.sin(self.angle_btwn_diagonals)

    def perimeter(self):
        side_a = MathHelpers.cosine_theorem(self.len_diag1 * self.ratio_intersect_diag1,
                                            self.len_diag2 * self.ratio_intersect_diag2,
                                            self.angle_btwn_diagonals)

        side_b = MathHelpers.cosine_theorem(self.len_diag1 * (1 - self.ratio_intersect_diag1),
                                            self.len_diag2 * self.ratio_intersect_diag2,
                                            math.pi - self.angle_btwn_diagonals)

        side_c = MathHelpers.cosine_theorem(self.len_diag1 * self.ratio_intersect_diag1,
                                            self.len_diag2 * (1 - self.ratio_intersect_diag2),
                                            self.angle_btwn_diagonals)

        side_d = MathHelpers.cosine_theorem(self.len_diag1 * (1 - self.ratio_intersect_diag1),
                                            self.len_diag2 * (1 - self.ratio_intersect_diag2),
                                            math.pi - self.angle_btwn_diagonals)

        return side_a + side_b + side_c + side_d

class RegularPentagon(ConvexPolygon):
    side = Length(name="Side of regular pentagon")
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return 0.25 * 5 * self.side * self.side * (1 / math.tan(0.2 * math.pi))

    def perimeter(self):
        return 5 * self.side

class RegularHexagon(ConvexPolygon):
    side = Length(name="Side of regular hexagon")

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return 0.5 * 3 * self.side * self.side * math.sqrt(3)

    def perimeter(self):
        return 6 * self.side

class RegularOctagon(ConvexPolygon):
    side = Length(name="Side of regular octagon")

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return 2 * (1 + math.sqrt(2)) * self.side * self.side

    def perimeter(self):
        return 8 * self.side


class IsoscelesTriangle(Triangle):
    def __init__(self, len_base, len_height):
        super().__init__(len_base, len_height, 0.5)

class EquilateralTriangle(Triangle):
    def __init__(self, len_side):
        super().__init__(len_side, (len_side * math.sqrt(3)) / 2, 0.5)

class Parallelogram(ConvexQuadrilateral):
    pass

class Kite(ConvexQuadrilateral):
    pass

class Rhombus(Parallelogram):
    pass

class Square(Rhombus):
    pass
