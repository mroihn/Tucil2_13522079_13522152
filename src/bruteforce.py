import time
import numpy as np
from plotting import *

curve_points = []
control_points = []
new_points= []
iteration = 0
             
# Fungsi bruteforce
def bruteforce(p0,p1,p2,n):
    global curve_points,new_points
    if n>1:
        for i in range(n):
            x = (1 - i/(n-1))**2 * p0[0] + 2 * (1 - i/(n-1)) * i/(n-1) * p1[0] + (i/(n-1))**2 * p2[0]
            y = (1 - i/(n-1))**2 * p0[1] + 2 * (1 - i/(n-1)) * i/(n-1) * p1[1] + (i/(n-1))**2 * p2[1]
            new_points.append([x,y])
            curve_points.append([x,y])
    else:   
        new_points.extend([p0,p1,p2])
        curve_points.extend([p0,p1,p2])
        
def main():
    global control_points,iteration
    # input titik kontrol
    print("Masukkan control point: ")
    p0 = tuple(map(float, input().split(" ")))
    p1 = tuple(map(float, input().split(" ")))
    p2 = tuple(map(float, input().split(" ")))

    # input jumlah iterasi
    iteration = int(input("Masukkan jumlah iterasi : "))
    
    temp = iteration
    for i in range( temp):
        if i==0 :
            iteration = 3
        else:
            iteration =iteration*2-1
    control_points.append(p0)
    control_points.append(p1)
    control_points.append(p2)

    start_time = time.time()
    bruteforce(p0,p1,p2,iteration)
    end_time = time.time()
    execution_time = end_time - start_time
    
    for i in new_points:
        print(i)
    print("Bezier Curve Points:")
    for point in curve_points:
        print(point)

    print("\nExecution Time:", execution_time, "seconds")
    plot_curve(control_points, new_points, curve_points)


if __name__ == "__main__":
    main()
