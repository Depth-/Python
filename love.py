#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as mp

x_coords = np.linspace(-100,100,500)
y_coords = np.linspace(-100,100,500)
points = []
for y in y_coords:
    for x in x_coords:
        if ((x * 0.03) ** 2 + (y * 0.03) ** 2 - 1) ** 3 - (x * 0.03) ** 2 * (y * 0.03) ** 3 <= 0:
            points.append({ "x": x, "y": y})
heart_x = list(map(lambda point: point["x"], points))
heart_y = list(map(lambda point: point["y"], points))
mp.scatter(heart_x, heart_y, s=10, alpha=0.5,c=range(len(heart_x)),cmap="Reds")
mp.show()
