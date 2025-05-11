import random
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


n = int(input("Enter the number of circles to draw: "))

circles = [(random.randint(10, 40), random.randint(10, 40), random.randint(5, 15)) for _ in range(n)]


def setPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()
    glFlush()


def drawCircle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r

    plotCirclePoints(xc, yc, x, y)

    while x <= y:
        x += 1
        if d < 0:
            d = d + 4 * x + 6
        else:
            y -= 1
            d = d + 4 * (x - y) + 10

        plotCirclePoints(xc, yc, x, y)


def plotCirclePoints(xc, yc, x, y):
    setPixel(xc + x, yc + y)
    setPixel(xc - x, yc + y)
    setPixel(xc + x, yc - y)
    setPixel(xc - x, yc - y)
    setPixel(xc + y, yc + x)
    setPixel(xc - y, yc + x)
    setPixel(xc + y, yc - x)
    setPixel(xc - y, yc - x)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3.0)

    for xc, yc, r in circles:
        drawCircle(xc, yc, r)

    glFlush()


def reshape(w, h):
    glViewport(0, 0, w, h)  # Set the viewport to the new window size
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Maintain the aspect ratio
    ratio = w / float(h)
    if w <= h:
        gluOrtho2D(0, 50, 0, 50 / ratio)
    else:
        gluOrtho2D(0, 50 * ratio, 0, 50)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 50, 0, 50)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(b"Circle Drawing - Brasenhum Algorithm")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)  # Add reshape callback to handle resizing
    glutMainLoop()


if __name__ == "__main__":
    main()
