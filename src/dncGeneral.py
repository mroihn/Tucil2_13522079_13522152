import time

from plotting import *

curve_points = []
control_points = []
mid_points = []
iteration = 0


# Fungsi untuk mendapatkan titik kurva
def solve(p0, p1, p2):
    global curve_points
    
    divide_conquer(p0, p1, p2, 0)
    


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

def dnc_general(p0,control_points,pk    ):#khusus untuk control point lebih dari sama dengan 2
    for i in range(len(control_points)):
        if i==0:
            curve_points.append(p0)
            solve(p0,control_points[i],control_points[i+1])
        elif i==len(control_points)-1:
            solve(control_points[i-1],control_points[i],pk)
            curve_points.append(pk)
        else:
            solve(control_points[i-1],control_points[i],control_points[i+1])
        # for i in curve_points()

def main():
    global control_points,iteration
    # input titik kontrol
    list_point = []
    print("Masukan jumlah control point(>2): ")
    number_control = int(input())
    for i in range(number_control):
        if i==0:
            p0 = tuple(map(float, input().split(" ")))
            control_points.append(p0)
        if i == number_control-1:
            pk = tuple(map(float, input().split(" ")))
            control_points.append(pk)
        if i!= 0 and i!= number_control-1:  
            p = tuple(map(float, input().split(" ")))  
            list_point.append(p)
            control_points.append(p)
   
    

    # input jumlah iterasi
    iteration = int(input("Masukkan jumlah iterasi : "))
    start_time = time.time()
    dnc_general(p0,list_point,pk)
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
