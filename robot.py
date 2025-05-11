from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

a1 = 0
a2 = 45

bx = -200
by = 0

dx1, dy1 = 150, 0   # shoulder to elbow
dx2, dy2 = 100, 0   # elbow to hand

def rotate(x, y, angle):
    rad = math.radians(angle)
    x_new = x * math.cos(rad) - y * math.sin(rad)
    y_new = x * math.sin(rad) + y * math.cos(rad)
    return x_new, y_new

def rotate_about_point(x, y, h, k, angle):
    x -= h
    y -= k
    x, y = rotate(x, y, angle)
    x += h
    y += k
    return x, y

def draw_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    if steps == 0:
        glBegin(GL_POINTS)
        glVertex2f(x1, y1)
        glEnd()
        return

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1
    for _ in range(steps + 1):
        glBegin(GL_POINTS)
        glVertex2f(round(x), round(y))
        glEnd()
        x += x_inc
        y += y_inc

def show():
    glClear(GL_COLOR_BUFFER_BIT)


    ex1, ey1 = bx + dx1, by + dy1
    x1, y1 = rotate_about_point(ex1, ey1, bx, by, a1)
    glColor3f(1, 0, 0)
    draw_line(bx, by, x1, y1)


    ex2, ey2 = x1 + dx2, y1 + dy2
    x2, y2 = rotate_about_point(ex2, ey2, x1, y1, a2)
    glColor3f(0, 0, 1)
    draw_line(x1, y1, x2, y2)

    glFlush()

def key(k, x, y):
    global a1, a2
    k = k.decode()
    if k == 's':
        a1 = (a1 + 5) % 360
    elif k == 'S':
        a1 = (a1 - 5) % 360
    elif k == 'e':
        a2 = (a2 + 5) % 360
    elif k == 'E':
        a2 = (a2 - 5) % 360
    glutPostRedisplay()

def start():
    glClearColor(1, 1, 1, 1)
    glColor3f(0, 0, 0)
    glPointSize(2)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -400, 400)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Arm with General Line Drawing")
    start()
    glutDisplayFunc(show)
    glutKeyboardFunc(key)
    glutMainLoop()

if __name__ == "__main__":
    main()
