# circle_drawer.py

import random
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

circles = []  # Global list to store circle (x, y, r)

def set_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def plot_circle_points(xc, yc, x, y):
    set_pixel(xc + x, yc + y)
    set_pixel(xc - x, yc + y)
    set_pixel(xc + x, yc - y)
    set_pixel(xc - x, yc - y)
    set_pixel(xc + y, yc + x)
    set_pixel(xc - y, yc + x)
    set_pixel(xc + y, yc - x)
    set_pixel(xc - y, yc - x)

def draw_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    plot_circle_points(xc, yc, x, y)

    while x <= y:
        x += 1
        if p < 0:
            p = p + 2 * x + 3
        else:
            p = p + 2 * (x - y) + 5
            y -= 1
        plot_circle_points(xc, yc, x, y)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Circle color: white
    glPointSize(3.0)

    for xc, yc, r in circles:
        draw_circle(xc, yc, r)

    glFlush()

def init_gl():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    gluOrtho2D(0, 500, 0, 500)

def start_M_circle_drawing():
    global circles
    n = int(input("Enter the number of circles to draw: "))
    circles = [(random.randint(100, 200), random.randint(100, 200),
                random.randint(50, 100)) for _ in range(n)]

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(b"Circle Drawing - Midpoint Algorithm")
    init_gl()
    glutDisplayFunc(display)
    glutMainLoop()
