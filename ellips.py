from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import sys

# Ask user for number of ellipses
n = int(input("Enter number of ellipses to draw: "))

ellipses = []

for i in range(n):
    a = random.randint(50, 100)    # Semi-major axis (width / 2)
    b = random.randint(30, 80)     # Semi-minor axis (height / 2)
    h = random.randint(-100, 100)  # X-coordinate of center
    k = random.randint(-100, 100)    # Y-coordinate of center

    print(f"Ellipse {i+1}: a = {a}, b = {b}, h = {h}, k = {k}")
    ellipses.append((a, b, h, k))

def setPixel(x, y, h, k):
    glBegin(GL_POINTS)
    glVertex2i(x + h, y + k)
    glVertex2i(-x + h, y + k)
    glVertex2i(x + h, -y + k)
    glVertex2i(-x + h, -y + k)
    glEnd()

def drawEllipse(a, b, h, k):
    x = 0
    y = b

    aa = a * a
    bb = b * b
    aa2 = 2 * aa
    bb2 = 2 * bb

    fx = 0
    fy = aa2 * b

    # Region 1
    p = int(bb - aa * b + 0.25 * aa)
    while fx < fy:
        setPixel(x, y, h, k)
        x += 1
        fx += bb2
        if p < 0:
            p += fx + bb
        else:
            y -= 1
            fy -= aa2
            p += fx + bb - fy

    # Region 2
    p = int(bb * (x + 0.5) ** 2 + aa * (y - 1) ** 2 - aa * bb)
    while y >= 0:
        setPixel(x, y, h, k)
        y -= 1
        fy -= aa2
        if p >= 0:
            p += -fy + aa
        else:
            x += 1
            fx += bb2
            p += fx - fy + aa

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    for a, b, h, k in ellipses:
        drawEllipse(a, b, h, k)
    glFlush()

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-200, 200, -200, 200)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Multiple Midpoint Ellipses (OpenGL)")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()
