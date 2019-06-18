import sys
from polygons import *
import params

class Menu:
    def __init__(self):
        self.options = {1: self.triangles,
                        2: self.quadrilaterals,
                        3: self.pentagon,
                        4: self.hexagon,
                        5: self.octagon,
                        6: self.quitme}

    @staticmethod
    def clear_console():
        print("\n"*128)

    def show_menu(self):
        while(True):
            Menu.clear_console()
            print("-"*28)
            print(" Program rysujący wielokąty")
            print("-"*28)
            print("""Co chcesz narysować?
            1. Trójkąty
            2. Czworokąty
            3. Pięciokąt foremny
            4. Sześciokąt foremny
            5. Ośmiokąt foremny
            6. Wyjście z programu
            """)
            option = input("1/2/3/4/5/6? ")
            try:
                selected = int(option)
                if selected not in self.options.keys():
                    print("Nieprawidłowa opcja!")
                else:
                    self.options[selected]()
            except Exception as e:
                print(f"Wystąpił błąd: {e}")
            _ = input("Aby kontynuować naciśnij ENTER")

    def triangles(self):
        print("""Dostępne figury:
        1. Dowolny trójkąt
        2. Trójkąt równoramienny
        3. Trójkąt równoboczny
        """)
        option = input("1/2/3? ")
        if option == "1":
            len_base = float(input("Podaj długość podstawy: "))
            len_h = float(input("Podaj wysokość: "))
            ratio_h = float(input("Podaj położenie wysokości na podstawie [0;1]"))
            poly = Triangle(len_base, len_h, ratio_h)
            Menu.draw_poly(poly)

        elif option == "2":
            len_base = float(input("Podaj długość podstawy: "))
            len_h = float(input("Podaj wysokość: "))
            poly = IsoscelesTriangle(len_base, len_h)
            Menu.draw_poly(poly)

        elif option == "3":
            len_base = float(input("Podaj długość boku: "))
            poly = EquilateralTriangle(len_base)
            Menu.draw_poly(poly)

        else:
            print("Nieprawidłowa opcja!")

    def quadrilaterals(self):
        print("""Dostępne figury:
        1. Dowolny czworokąt wypukły
        2. Równoległobok
        3. Deltoid
        4. Romb
        5. Kwadrat
        """)

        option = input("1/2/3/4/5? ")

        if option == "1":
            len_diag1 = float(input("Długość pierwszej przekątnej: "))
            len_diag2 = float(input("Długość drugiej przekątnej: "))
            ratio_diag1 = float(input("Stosunek przecięcia pierwszej przekątnej przez drugą? [0;1] "))
            ratio_diag2 = float(input("Stosunek przecięcia drugiej pzekątnej przez pierwszą? [0;1] "))
            angle_diags = float(input("Kąt między przekątnymi (w stopniach)? "))

            poly = ConvexQuadrilateral(len_diag1, len_diag2, ratio_diag1, ratio_diag2, math.radians(angle_diags))
            Menu.draw_poly(poly)

        elif option == "2":
            len_side_a = float(input("Długość jednego boku? "))
            len_side_b = float(input("Długość drugiego boku? "))
            angle_sides = float(input("Kąt ostry między bokami (w stopniach)? "))

            poly = Parallelogram(len_side_a, len_side_b, math.radians(angle_sides))
            Menu.draw_poly(poly)

        elif option == "3":
            len_diag1 = float(input("Długość pierwszej przekątnej: "))
            len_diag2 = float(input("Długość drugiej przekątnej: "))
            ratio_diag1 = float(input("Stosunek przecięcia pierwszej przekątnej przez drugą? [0;1] "))

            poly = Kite(len_diag1, len_diag2, ratio_diag1)
            Menu.draw_poly(poly)

        elif option == "4":
            len_side = float(input("Długość boku? "))
            angle_sides = float(input("Kąt ostry między bokami (w stopniach)? "))
            poly = Rhombus(len_side, math.radians(angle_sides))
            Menu.draw_poly(poly)

        elif option == "5":
            len_side = float(input("Długość boku? "))
            poly = Square(len_side)
            Menu.draw_poly(poly)

        else:
            print("Nieprawidłowa opcja!")

    def pentagon(self):
        len_side = float(input("Długość boku? "))
        poly = RegularPentagon(len_side)
        Menu.draw_poly(poly)

    def hexagon(self):
        len_side = float(input("Długość boku? "))
        poly = RegularHexagon(len_side)
        Menu.draw_poly(poly)

    def octagon(self):
        len_side = float(input("Długość boku? "))
        poly = RegularOctagon(len_side)
        Menu.draw_poly(poly)

    def quitme(self):
        sys.exit(0)

    @staticmethod
    def draw_poly(poly: ConvexPolygon):
        print("Dostępne kolory: ", end="")
        for key in params.AVAILABLE_COLOURS.keys():
            print(key, end=" ")
        print("")
        colour_f = input("Kolor wypełnienia [domyślny: white]? ")
        colour_o = input("Kolor obramowania [domyślny: black]? ")

        if (len(colour_f) < 1):
            colour_f = "white"
        if (len(colour_o) < 1):
            colour_o = "black"

        scaleI = input("Skala rysunku [domyślnie: 1]?")
        if len(scaleI) < 1:
            scale = 1.0
        else:
            scale = float(scaleI)

        poly.set_fill_colour(colour_f)
        poly.set_outline_colour(colour_o)
        poly.draw(scale)

if __name__ == '__main__':
    menu = Menu()
    menu.show_menu()