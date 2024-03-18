import matplotlib.pyplot as plt

def plot_curve(control_points, mid_points, curve_points):
    x_points = []
    y_points = []
    for step_points in control_points:
        x_points.append(step_points[0])
        y_points.append(step_points[1])

        plt.title("Bezier Curve (Step by Step)")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.scatter(x_points, y_points, color="red")
        plt.pause(0.15)
        plt.plot(x_points, y_points, "-o", color="black", markerfacecolor="red")
        plt.pause(0.15)
    plot_mid_point(mid_points)
    plot_curve_point(curve_points)
    plt.show()

 
def plot_mid_point(mid_points):
    x_points = []
    y_points = []
    for step_points in mid_points:
        x_points.append(step_points[0])
        y_points.append(step_points[1])

        plt.title("Quadratic Bezier Curve (Step by Step)")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.scatter(x_points, y_points, color="grey")
        plt.pause(0.15)
        plt.plot(x_points, y_points, "-o", color="silver", markerfacecolor="grey")
        plt.pause(0.15)


def plot_curve_point(curve_points):
    x_points = []
    y_points = []
    for step_points in curve_points:
        x_points.append(step_points[0])
        y_points.append(step_points[1])

        plt.title("Quadratic Bezier Curve (Step by Step)")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.scatter(x_points, y_points, color="midnightblue")
        plt.pause(0.15)
        plt.plot(x_points, y_points, "-o", color="navy", markerfacecolor="midnightblue")
        plt.pause(0.15)
