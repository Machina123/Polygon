import numbers
import math

AVAILABLE_COLOURS = {"red": "#ff0000", "green": "#00ff00", "blue": "#0000ff", "magenta": "#ff00ff",
                     "yellow": "#ffff00", "cyan": "#00ffff", "black": "#000000", "white": "#ffffff"}

class Length:
    """Deskryptor długości boku figury"""

    def __init__(self, initial = None, name = "Length"):
        self.val = initial
        self.name = name

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Real):
            raise TypeError(f"{self.name} is expected to be of type Real, {type(value)} given")
        elif value <= 0:
            raise ValueError(f"{self.name} is expected to be positive real number, {value} given")
        self.val = value


class Colour:
    """Deskryptor wartości koloru"""

    def __init__(self, initial = None, name = "Colour"):
        self.val = initial
        self.name = name

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        if not value in AVAILABLE_COLOURS.keys():
            if not str(value).lower() in AVAILABLE_COLOURS.values():
                raise ValueError(f"{self.name} is expected to be of known colour value, {value} given")
            else:
                self.val = value
        else:
            self.val = AVAILABLE_COLOURS[value]


class Angle:
    """Deskryptor wartości kąta (w radianach) - [0; 2*Pi)"""

    def __init__(self, initial = None, name = "Angle"):
        self.val = initial
        self.name = name

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Real):
            raise TypeError(f"{self.name} is expected to be of type Real, {type(value)} given")
        elif not (0 <= value < 2 * math.pi):
            raise ValueError(f"{self.name} is expected to be between 0 (inc.) and 2*Pi, {value} given")
        self.val = value

class Ratio:
    """Deskryptor wartości podziału - [0;1]"""

    def __init__(self, initial = None, name = "Ratio"):
        self.val = initial
        self.name = name

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Real):
            raise TypeError(f"{self.name} is expected to be of type Real, {type(value)} given")
        elif not (0 <= value <= 1):
            raise ValueError(f"{self.name} is expected to be between 0 and 1, {value} given")
        self.val = value


class MathHelpers:

    @staticmethod
    def cosine_law(a, b, phi):
        return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(phi))
