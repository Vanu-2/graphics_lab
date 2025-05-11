from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

# Global options and values
shape_option = 1
transform_option = 1
angle_deg = 0
tx, ty = 0, 0
sx, sy = 1, 1
scale_radius = 1

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, 800, 0, 600)


def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def draw_circle(cx, cy, r):
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        theta = math.radians(i)
        x = cx + r * math.cos(theta)
        y = cy + r * math.sin(theta)
        glVertex2f(x, y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    if shape_option == 1:  # Line
        x1, y1 = 200, 200
        x2, y2 = 400, 400

        if transform_option == 1:  # Translation
            glColor3f(0, 1, 1)
            draw_line(x1, y1, x2, y2)
            glColor3f(1, 0, 0)
            draw_line(x1 + tx, y1 + ty, x2 + tx, y2 + ty)

        elif transform_option == 2:  # Rotation
            angle_rad = math.radians(angle_deg)
            x2r = x1 + ((x2 - x1) * math.cos(angle_rad) - (y2 - y1) * math.sin(angle_rad))
            y2r = y1 + ((x2 - x1) * math.sin(angle_rad) + (y2 - y1) * math.cos(angle_rad))
            glColor3f(0, 1, 1)
            draw_line(x1, y1, x2, y2)
            glColor3f(1, 1, 0)
            draw_line(x1, y1, x2r, y2r)

        elif transform_option == 3:  # Scaling
            glColor3f(1, 1, 1)
            draw_line(x1, y1, x2, y2)
            glColor3f(0, 1, 0)
            draw_line(x1 * sx, y1 * sy, x2 * sx, y2 * sy)

        elif transform_option == 4:  # Reflection
            glColor3f(0, 1, 1)
            draw_line(x1, y1, x2, y2)
            glColor3f(1, 0, 1)
            draw_line(x1, 600 - y1, x2, 600 - y2)

    elif shape_option == 2:  # Circle
        cx, cy, r = 300, 300, 50

        if transform_option == 1:  # Translation
            glColor3f(0, 1, 1)
            draw_circle(cx, cy, r)
            glColor3f(1, 0, 0)
            draw_circle(cx + tx, cy + ty, r)

        elif transform_option == 2:  # Rotation
            angle_rad = math.radians(angle_deg)
            cxr = cx * math.cos(angle_rad) - cy * math.sin(angle_rad)
            cyr = cx * math.sin(angle_rad) + cy * math.cos(angle_rad)
            glColor3f(0, 1, 1)
            draw_circle(cx, cy, r)
            glColor3f(1, 1, 0)
            draw_circle(cxr, cyr, r)

        elif transform_option == 3:  # Scaling (radius)
            glColor3f(0, 1, 1)
            draw_circle(cx, cy, r)
            glColor3f(0, 1, 0)
            draw_circle(cx, cy, r * scale_radius)

        elif transform_option == 4:  # Reflection
            glColor3f(0, 1, 1)
            draw_circle(cx, cy, r)
            glColor3f(1, 0, 1)
            draw_circle(cx, 600 - cy, r)

    glFlush()


def main():
    global shape_option, transform_option
    global angle_deg, tx, ty, sx, sy, scale_radius

    print("Choose a shape:")
    print("1. Line")
    print("2. Circle")
    shape_option = int(input("Selection: "))

    print("\nChoose a transformation:")
    print("1. Translation")
    print("2. Rotation")
    print("3. Scaling")
    print("4. Reflection")
    transform_option = int(input("Selection: "))

    if transform_option == 1:
        tx = int(input("Enter tx: "))
        ty = int(input("Enter ty: "))
    elif transform_option == 2:
        angle_deg = float(input("Enter angle in degrees: "))
    elif transform_option == 3:
        if shape_option == 1:
            sx = float(input("Enter sx: "))
            sy = float(input("Enter sy: "))
        else:
            scale_radius = float(input("Enter scaling factor for radius: "))

    # GLUT Window Setup
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"2D Transformations - Line and Circle")
    init()
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
