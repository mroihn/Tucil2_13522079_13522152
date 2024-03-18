import time
from plotting import *

curve_points = []
control_points = []
mid_points = []
iteration = 0
x_points = []
y_points = []

# Fungsi untuk mendapatkan titik kurva
def solve(control_points):
    global curve_points
    curve_points.append(control_points[0])
    bezier_curve(control_points, 0)
    curve_points.append(control_points[len(control_points) - 1])

# Fungsi divide and conquer
def bezier_curve(control_points, iterationNow):
    global curve_points
    if iterationNow < iteration:
        right = control_points.copy()
        left = control_points.copy()
        left = left[::-1]
        n = len(control_points) - 1
        while(n > 0):
            for i in range (n):
                right[i] = [(right[i][0] + right[i+1][0]) / 2, (right[i][1] + right[i+1][1]) / 2]
                left[i] = [(left[i][0] + left[i+1][0]) / 2, (left[i][1] + left[i+1][1]) / 2]
                mid_points.append(right[i])
            n-=1

        iterationNow+=1
        left = left[::-1]
        # kiri
        bezier_curve(left, iterationNow)
        curve_points.append(right[0])
        # kanan
        bezier_curve(right, iterationNow)


def main():
    global iteration,n
    # Input titik kontrol
    print("Masukkan jumlah titik kontrol:")
    n = int(input())
    points = []
    for i in range(n):
        point = tuple(map(float, input(f"Masukkan titik ke-{i+1}: ").split(" ")))
        points.append(point)
        control_points.append(point)

    iteration = int(input("Masukkan jumlah iterasi : "))

    start_time = time.time()
    solve(points)
    end_time = time.time()
    execution_time = end_time - start_time

    print("Bezier Curve Points:")
    for point in curve_points:
        print(point)

    print("\nExecution Time:", execution_time, "seconds")
    plot_curve(control_points, mid_points, curve_points)


if __name__ == "__main__":
    main()
