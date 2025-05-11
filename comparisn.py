import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import random
import time


def draw_point(x, y, color):
    gl.glColor3f(color[0], color[1], color[2])
    gl.glBegin(gl.GL_POINTS)
    gl.glVertex2f(x, y)
    gl.glEnd()


def draw_bresenham_circle(x_center, y_center, radius, color):
    x = 0
    y = radius
    p = 3 - 2 * radius

    while x <= y:

        draw_point(x_center + x, y_center - y, color)
        draw_point(x_center + y, y_center - x, color)
        draw_point(x_center - y, y_center - x, color)
        draw_point(x_center - x, y_center - y, color)
        draw_point(x_center - x, y_center + y, color)
        draw_point(x_center - y, y_center + x, color)
        draw_point(x_center + y, y_center + x, color)
        draw_point(x_center + x, y_center + y, color)

        x += 1

        if p > 0:
            y -= 1
            p = p + 4 * (x - y) + 10
        else:
            p = p + 4 * x + 6


def draw_midpoint_circle(x_center, y_center, radius, color):
    x = radius
    y = 0
    p = 1 - radius

    while x >= y:

        draw_point(x_center + x, y_center - y, color)
        draw_point(x_center + y, y_center - x, color)
        draw_point(x_center - y, y_center - x, color)
        draw_point(x_center - x, y_center - y, color)
        draw_point(x_center - x, y_center + y, color)
        draw_point(x_center - y, y_center + x, color)
        draw_point(x_center + y, y_center + x, color)
        draw_point(x_center + x, y_center + y, color)

        y += 1

        if p <= 0:
            p = p + 2 * y + 1
        else:
            x -= 1
            p = p + 2 * y - 2 * x + 1


def random_color():
    return (random.random(), random.random(), random.random())


def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


def init_window():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
    glut.glutInitWindowSize(400, 400)
    glut.glutCreateWindow("Bresenham vs Midpoint Circle Drawing")
    glu.gluOrtho2D(0.0, 400.0, 0.0, 400.0)
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)


def display():
    circle_radius = random.randint(10, 50)
    center_x = 200
    center_y = 200


    bresenham_time = measure_time(draw_bresenham_circle, center_x, center_y, circle_radius, random_color())
    midpoint_time = measure_time(draw_midpoint_circle, center_x, center_y, circle_radius, random_color())

    print("Bresenham Circle Drawing Time:", bresenham_time, "seconds")
    print("Midpoint Circle Drawing Time:", midpoint_time, "seconds")

    glut.glutSwapBuffers()


def main():
    init_window()
    glut.glutDisplayFunc(display)
    glut.glutMainLoop()


if __name__ == "__main__":
    main()
