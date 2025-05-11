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

# Object position
obj_x, obj_y = 100, 100

# Reaching flag
reaching = False

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

def get_hand_position():
    ex1, ey1 = bx + dx1, by + dy1
    x1, y1 = rotate_about_point(ex1, ey1, bx, by, a1)

    ex2, ey2 = x1 + dx2, y1 + dy2
    x2, y2 = rotate_about_point(ex2, ey2, x1, y1, a2)

    return x1, y1, x2, y2

def draw_object():
    glColor3f(0, 1, 0)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex2f(obj_x, obj_y)
    glEnd()
    glPointSize(2)

def show():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw arm
    x1, y1, x2, y2 = get_hand_position()
    glColor3f(1, 0, 0)
    draw_line(bx, by, x1, y1)
    glColor3f(0, 0, 1)
    draw_line(x1, y1, x2, y2)

    # Draw object
    draw_object()

    glFlush()

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def try_reach():
    global a1, a2

    # Current hand position
    _, _, hx, hy = get_hand_position()

    # Calculate current distance
    current_dist = distance(hx, hy, obj_x, obj_y)

    # Try small angle adjustments
    best_a1, best_a2 = a1, a2
    min_dist = current_dist

    for da1 in [-2, 0, 2]:
        for da2 in [-2, 0, 2]:
            temp_a1 = (a1 + da1) % 360
            temp_a2 = (a2 + da2) % 360

            # Calculate new hand position
            ex1, ey1 = bx + dx1, by + dy1
            x1, y1 = rotate_about_point(ex1, ey1, bx, by, temp_a1)
            ex2, ey2 = x1 + dx2, y1 + dy2
            x2, y2 = rotate_about_point(ex2, ey2, x1, y1, temp_a2)

            d = distance(x2, y2, obj_x, obj_y)
            if d < min_dist:
                min_dist = d
                best_a1, best_a2 = temp_a1, temp_a2

    a1, a2 = best_a1, best_a2

    glutPostRedisplay()

def key(k, x, y):
    global a1, a2, reaching
    k = k.decode()
    if k == 's':
        a1 = (a1 + 5) % 360
    elif k == 'S':
        a1 = (a1 - 5) % 360
    elif k == 'e':
        a2 = (a2 + 5) % 360
    elif k == 'E':
        a2 = (a2 - 5) % 360
    elif k == 'r':  # Start reaching the object
        reaching = True
    glutPostRedisplay()

def timer(value):
    if reaching:
        try_reach()
    glutTimerFunc(50, timer, 0)

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
    glutCreateWindow(b"Arm Reaching Object")
    start()
    glutDisplayFunc(show)
    glutKeyboardFunc(key)
    glutTimerFunc(50, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
