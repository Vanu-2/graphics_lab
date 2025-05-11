# line_drawer.py
import random
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

lines = []  # Global list to store line coordinates

def set_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def draw_dda():
    for x1, y1, x2, y2 in lines:
        dx = x2 - x1
        dy = y2 - y1

        if dx == 0:  # vertical line
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                set_pixel(x1, y)
        else:
            m = dy / dx
            if abs(m) <= 1:
                if x1 > x2:
                    x1, x2, y1, y2 = x2, x1, y2, y1
                y = y1
                for x in range(x1, x2 + 1):
                    set_pixel(x, round(y))
                    y += m
            else:
                if y1 > y2:
                    x1, x2, y1, y2 = x2, x1, y2, y1
                x_f = x1
                for y in range(y1, y2 + 1):
                    set_pixel(int(x_f + 0.5), y)
                    x_f += 1 / m

    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3.0)
    draw_dda()
    glFlush()

def init_gl():
    glClearColor(0.0, 0.0, 255.0, 1.0)
    gluOrtho2D(0, 400, 0, 400)

def start_DDA_line_drawing():
    global lines
    n = int(input("Enter the number of lines to draw: "))
    lines = [(random.randint(0, 400), random.randint(0, 400),
              random.randint(0, 400), random.randint(0, 400)) for _ in range(n)]

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(b"Line Drawing - DDA")
    init_gl()
    glutDisplayFunc(display)
    glutMainLoop()
