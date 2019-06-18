import constants
import polygons
import tkinter as tk
import math

class GUI:

    @staticmethod
    def get_rotated_point(x, y, angle):
        xp = x * math.cos(angle) - y * math.sin(angle)
        yp = x * math.sin(angle) + y * math.cos(angle)
        return (xp, yp)

    @staticmethod
    def center_window(wnd: tk.Tk):
        sw = wnd.winfo_screenwidth()
        sh = wnd.winfo_screenheight()
        ww = constants.WINDOW_WIDTH
        wh = constants.WINDOW_HEIGHT
        wnd.geometry(f"{ww}x{wh}+{sw//2 - ww//2}+{sh//2 - wh//2}")

    @staticmethod
    def draw_polygon(poly_cls, coords: list, scale):
        window = tk.Tk()
        canvas = tk.Canvas(window, width=constants.WINDOW_WIDTH, height=constants.WINDOW_HEIGHT)
        canvas.pack()
        GUI.center_window(window)
        rotated_coords = list()
        for point in coords:
            rotated_point = GUI.get_rotated_point(point[0], point[1], math.pi)
            if isinstance(poly_cls, polygons.ConvexQuadrilateral):
                rotated_coords.append(GUI.get_rotated_point(rotated_point[0], rotated_point[1], math.pi/4))
            else:
                rotated_coords.append(rotated_point)

        canvas.create_text(10, 10, text=f"Figura: {poly_cls.__class__.__name__}", anchor="nw")
        canvas.create_text(10, 25, text=f"Pole figury: {poly_cls.area()}", anchor="nw")
        canvas.create_text(10, 40, text=f"Obwód figury: {poly_cls.perimeter()}", anchor="nw")
        canvas.create_text(10, 55, text=f"Skala rysunku: {str(scale)}", anchor="nw")

        canvas.create_polygon(rotated_coords, tag="polygon", fill=poly_cls.fill_colour,
                              outline=poly_cls.outline_colour)

        x1, y1, x2, y2 = canvas.bbox("polygon")
        print((x1,y1,x2,y2))
        if (-1 < ((x2-x1)/2) < 1)  and (-1 < ((y2-y1)/2) < 1):
            canvas.move("polygon", (x2-x1)/2, (y2-y1)/2)
        c_center_x, c_center_y = constants.WINDOW_WIDTH//2, constants.WINDOW_HEIGHT//2
        canvas.move("polygon", c_center_x, c_center_y)
        tk.mainloop()
