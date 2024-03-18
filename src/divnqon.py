import time

from plotting import *

curve_points = []
control_points = []
mid_points = []
iteration = 0


# Fungsi untuk mendapatkan titik kurva
def solve(p0, p1, p2):
    global curve_points
    curve_points.append(p0)
    divide_conquer(p0, p1, p2, 0)
    curve_points.append(p2)


# Fungsi divide and conquer
def divide_conquer(p0, p1, p2, iterationNow):
    global curve_points,mid_points
    if iterationNow < iteration:
        mid1 = [(p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2]
        mid2 = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
        mid = [(mid1[0] + mid2[0]) / 2, (mid1[1] + mid2[1]) / 2]
        mid_points.append(mid1)
        mid_points.append(mid2)
        mid_points.append(mid)

        iterationNow += 1
        # kiri
        divide_conquer(p0, mid1, mid, iterationNow)
        curve_points.append(mid)
        # kanan
        divide_conquer(mid, mid2, p2, iterationNow)
    
def main():
    global control_points,iteration
    # input titik kontrol
    print("Masukkan control point: ")
    p0 = tuple(map(float, input().split(" ")))
    p1 = tuple(map(float, input().split(" ")))
    p2 = tuple(map(float, input().split(" ")))
 
    # input jumlah iterasi
    iteration = int(input("Masukkan jumlah iterasi : "))
    control_points.append(p0)
    control_points.append(p1)
    control_points.append(p2)

    start_time = time.time()
    solve(p0, p1, p2)
    end_time = time.time()
    execution_time = end_time - start_time
    for i in mid_points:
        print(i)
    print("Bezier Curve Points:")
    for point in curve_points:
        print(point)

    print("\nExecution Time:", execution_time, "seconds")
    plot_curve(control_points, mid_points, curve_points)


if __name__ == "__main__":
    main()
