# bresenham_drawer.py

import random
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

lines = []  # Global list to store lines

def set_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def draw_bresenham():
    for x1, y1, x2, y2 in lines:
        dx = x2 - x1
        dy = y2 - y1

        if dx < 0:
            x1, x2, y1, y2 = x2, x1, y2, y1
            dx = -dx
            dy = -dy

        x, y = x1, y1

        if abs(dx) > abs(dy):  # slope < 1
            d = 2 * abs(dy) - abs(dx)
            inc1 = 2 * abs(dy)
            inc2 = 2 * (abs(dy) - abs(dx))

            set_pixel(x, y)

            while x < x2:
                x += 1
                if d < 0:
                    d += inc1
                else:
                    d += inc2
                    y += 1 if dy > 0 else -1
                set_pixel(x, y)

        else:  # slope >= 1
            d = 2 * abs(dx) - abs(dy)
            inc1 = 2 * abs(dx)
            inc2 = 2 * (abs(dx) - abs(dy))

            set_pixel(x, y)

            while y != y2:
                y += 1 if dy > 0 else -1
                if d < 0:
                    d += inc1
                else:
                    d += inc2
                    x += 1
                set_pixel(x, y)

    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(2.0)
    draw_bresenham()
    glFlush()

def init_gl():
    glClearColor(0.0, 0.0, 255.0, 1.0)
    gluOrtho2D(0, 800, 0, 800)

def start_B_line_drawing():
    global lines
    n = int(input("Enter the number of lines to draw (Bresenham): "))
    lines = [(random.randint(0, 500), random.randint(0, 500),
              random.randint(0, 500), random.randint(0, 500)) for _ in range(n)]

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(b"Line Drawing - Bresenham")
    init_gl()
    glutDisplayFunc(display)
    glutMainLoop()
