import random
import matplotlib.pyplot as plt


def draw_lines(num_lines):
    plt.figure(figsize=(8, 6))

    for _ in range(num_lines):
        xs = random.randint(-20, 20)
        ys = random.randint(-20, 20)
        xe = random.randint(-20, 20)
        ye = random.randint(-20, 20)
        c = random.randint(-20, 20)

        if xs != xe:  # Not a vertical line
            m = (ye - ys) / (xe - xs)

            # Plot each point as it is calculated
            if xs < xe:
                x_range = range(xs, xe + 1)
            else:
                x_range = range(xs, xe - 1, -1)

            for x in x_range:
                y = m * x + c  # Calculate y
                plt.plot(x, y, marker='o', color='b')  # Plot the point

        else:  # Vertical line (x doesn't change)
            m = float('inf')
            y_vals = range(min(ys, ye), max(ys, ye) + 1)
            for y in y_vals:
                plt.plot(xs, y, marker='o', color='b')  # Plot the point

        # Add a small pause to ensure the plot updates immediately after each point is plotted
        plt.pause(0.01)  # Adjust the pause duration if needed

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Randomly Generated Lines with Incremented X-values")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    num_lines = int(input("Enter the number of lines to draw: "))
    draw_lines(num_lines)
