from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Arm segment lengths
L1 = 100
L2 = 75

# Target position
target_x = 120
target_y = 50

# Joint angles (initial)
theta1 = 0
theta2 = 0

# Target angles
target_theta1 = 0
target_theta2 = 0

# Speed of angle change per frame
step = 1.0

# ----------------------
# Transformation Helpers
# ----------------------

def deg_to_rad(deg):
    return deg * math.pi / 180.0

def rotate(x, y, angle_deg):
    """Rotate (x, y) counterclockwise around origin by angle (deg)."""
    rad = deg_to_rad(angle_deg)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    x_new = x * cos_a - y * sin_a
    y_new = x * sin_a + y * cos_a
    return x_new, y_new

def translate(x, y, dx, dy):
    return x + dx, y + dy

# ----------------------
# Inverse Kinematics Solver (for target angles)
# ----------------------

def compute_target_angles():
    global target_theta1, target_theta2
    dx = target_x
    dy = target_y
    d = math.hypot(dx, dy)
    d = min(max(d, 0.0001), L1 + L2)

    cos_theta2 = (d**2 - L1**2 - L2**2) / (2 * L1 * L2)
    cos_theta2 = max(min(cos_theta2, 1), -1)
    theta2_rad = math.acos(cos_theta2)

    k1 = L1 + L2 * math.cos(theta2_rad)
    k2 = L2 * math.sin(theta2_rad)
    theta1_rad = math.atan2(dy, dx) - math.atan2(k2, k1)

    target_theta1 = math.degrees(theta1_rad)
    target_theta2 = math.degrees(theta2_rad)

# ----------------------
# Animation Update
# ----------------------

def update_angles():
    global theta1, theta2

    if abs(theta1 - target_theta1) > step:
        theta1 += step if theta1 < target_theta1 else -step
    else:
        theta1 = target_theta1

    if abs(theta2 - target_theta2) > step:
        theta2 += step if theta2 < target_theta2 else -step
    else:
        theta2 = target_theta2

# ----------------------
# Drawing Functions
# ----------------------

def draw_circle(cx, cy, r):
    glBegin(GL_POLYGON)
    for i in range(32):
        angle = 2 * math.pi * i / 32
        glVertex2f(cx + r * math.cos(angle), cy + r * math.sin(angle))
    glEnd()

def draw_robot_arm():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)

    # Base joint A
    ax, ay = 0, 0

    # Joint B position
    bx, by = rotate(L1, 0, theta1)
    bx, by = translate(bx, by, ax, ay)

    # End effector C position
    cx_local, cy_local = rotate(L2, 0, theta1 + theta2)
    cx, cy = translate(cx_local, cy_local, bx, by)

    # Segment A -> B
    glLineWidth(3)
    glColor3f(0.2, 0.8, 1)
    glBegin(GL_LINES)
    glVertex2f(ax, ay)
    glVertex2f(bx, by)
    glEnd()

    # Segment B -> C
    glColor3f(0.8, 1, 0.2)
    glBegin(GL_LINES)
    glVertex2f(bx, by)
    glVertex2f(cx, cy)
    glEnd()

    # Draw joints
    glColor3f(1, 1, 1)
    draw_circle(ax, ay, 4)
    draw_circle(bx, by, 4)
    draw_circle(cx, cy, 4)

    # Draw target
    glColor3f(1, 0, 0)
    glPointSize(6)
    glBegin(GL_POINTS)
    glVertex2f(target_x, target_y)
    glEnd()

    glutSwapBuffers()

# ----------------------
# GLUT Setup
# ----------------------

def update(value):
    update_angles()
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-200, 200, -200, 200)
    glMatrixMode(GL_MODELVIEW)

def main():
    compute_target_angles()
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Practical 2D Robotic Hand (Manual Transformations)")
    glutDisplayFunc(draw_robot_arm)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, update, 0)
    glClearColor(0.05, 0.05, 0.05, 1)
    glutMainLoop()

if __name__ == '__main__':
    main()
