# circle_drawer.py
import random
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

circles = []  # Global list to hold circle data

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
    d = 3 - 2 * r
    plot_circle_points(xc, yc, x, y)

    while x <= y:
        x += 1
        if d < 0:
            d = d + 4 * x + 6
        else:
            y -= 1
            d = d + 4 * (x - y) + 10
        plot_circle_points(xc, yc, x, y)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3.0)

    for xc, yc, r in circles:
        draw_circle(xc, yc, r)

    glFlush()

def init_gl():
    glClearColor(0.0, 0.0, 255.0, 1.0)
    gluOrtho2D(0, 800, 0, 800)

def start_B_circle_drawing():
    global circles
    num = int(input("Enter the number of circles to draw: "))
    circles = [(random.randint(100, 400), random.randint(100, 400), random.randint(50, 150)) for _ in range(num)]

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(b"Circle Drawing - Bresenham Algorithm")
    init_gl()
    glutDisplayFunc(display)
    glutMainLoop()
