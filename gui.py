import constants
import tkinter as tk
import math

class GUI:

    @staticmethod
    def get_rotated_point(x, y, angle):
        xp = x * math.cos(angle) - y * math.sin(angle)
        yp = x * math.sin(angle) + y * math.cos(angle)
        return (xp, yp)

    @staticmethod
    def draw_polygon(poly_cls, coords: list, fill_colour, outline_colour, scale):
        window = tk.Tk()
        canvas = tk.Canvas(window, width=constants.WINDOW_WIDTH, height=constants.WINDOW_HEIGHT)
        canvas.pack()
        rotated_coords = list()
        for point in coords:
            rotated_coords.append(GUI.get_rotated_point(point[0], point[1], math.pi))
        print(rotated_coords)
        canvas.create_text(10, 10, text=f"Figura: {poly_cls.__class__.__name__}", anchor="nw")
        canvas.create_text(10, 25, text=f"Pole figury: {poly_cls.area()}", anchor="nw")
        canvas.create_text(10, 40, text=f"Obwód figury: {poly_cls.perimeter()}", anchor="nw")
        canvas.create_text(10, 55, text=f"Skala rysunku: {str(scale)}", anchor="nw")
        canvas.create_polygon(rotated_coords, tag="polygon", fill=fill_colour, outline=outline_colour, width=2)
        x1, y1, x2, y2 = canvas.bbox("polygon")
        canvas.move("polygon", (x2-x1)/2, (y2-y1)/2)
        c_center_x, c_center_y = constants.WINDOW_WIDTH//2, constants.WINDOW_HEIGHT//2
        canvas.move("polygon", c_center_x, c_center_y)
        tk.mainloop()
