import random
import matplotlib.pyplot as plt
import numpy as np



def plot_circle(center, radius, color):

    a, b = center
    x_vals = np.arange(a - radius, a + radius + 1, 1)
    y_vals_top = []
    y_vals_bottom = []

    for x in x_vals:
        y1 = b + (radius ** 2 - (x - a) ** 2) ** 0.5
        y2 = b - (radius ** 2 - (x - a) ** 2) ** 0.5
        y_vals_top.append(y1)
        y_vals_bottom.append(y2)

    plt.plot(x_vals, y_vals_top, color=color)
    plt.plot(x_vals, y_vals_bottom, color=color)


def generate_circles(n):

    plt.figure(figsize=(10, 8))
    min_x, max_x, min_y, max_y = float('inf'), float('-inf'), float('inf'), float('-inf')

    for _ in range(n):
        center = (random.randint(5, 15), random.randint(5, 15))
        radius = random.randint(10, 25)
        color = np.random.rand(3, )

        plot_circle(center, radius, color)

        min_x = min(min_x, center[0] - radius)
        max_x = max(max_x, center[0] + radius)
        min_y = min(min_y, center[1] - radius)
        max_y = max(max_y, center[1] + radius)

    plt.xlim(min_x - 2, max_x + 2)
    plt.ylim(min_y - 2, max_y + 2)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Random Circles")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


def circle():
    num = int(input("Enter number of circles: "))
    generate_circles(num)
