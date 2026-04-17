#!/usr/bin/env -S python3 -B

from pathlib import Path
from time import time

from common.r3 import R3
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


def draw_plane_y_minus_1(p, tk):
    y = -1
    size = 300  # размер "плоскости"

    v1 = R3(-size, (y - 2) * p.koef_dist, -size)
    v2 = R3(size, (y - 2) * p.koef_dist, -size)
    v3 = R3(size, (y - 2) * p.koef_dist, size)
    v4 = R3(-size, (y - 2) * p.koef_dist, size)

    v5 = R3(-size, (y + 2) * p.koef_dist, -size)
    v6 = R3(size, (y + 2) * p.koef_dist, -size)
    v7 = R3(size, (y + 2) * p.koef_dist, size)
    v8 = R3(-size, (y + 2) * p.koef_dist, size)

    # рисуем первый квадрат (плоскость) y - 2
    tk.draw_line(v1, v2)
    tk.draw_line(v2, v3)
    tk.draw_line(v3, v4)
    tk.draw_line(v4, v1)

    # рисуем второй квадрат (плоскость) y + 2
    tk.draw_line(v5, v6)
    tk.draw_line(v6, v7)
    tk.draw_line(v7, v8)
    tk.draw_line(v8, v5)


def draw_good_points(p, tk):
    for v in p.vertexes:
        if v.y > 1 * p.koef_dist or v.y < -3 * p.koef_dist:
            # маленький крестик
            d = 5
            tk.draw_line(R3(v.x - d, v.y, v.z), R3(v.x + d, v.y, v.z))
            tk.draw_line(R3(v.x, v.y - d, v.z), R3(v.x, v.y + d, v.z))


tk = TkDrawer()
try:
    for name in ["ccc", "cube", "box", "box10", "box10a",
                 "cube10", "cube10a", "piramid"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        p = Polyedr(Path(__file__).parent / "data" / f"{name}.geom")
        print("Сумма площадей:", p.good_facets_area())
        p.draw(tk)
        draw_plane_y_minus_1(p, tk)
        draw_good_points(p, tk)
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
