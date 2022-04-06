from math import degrees, pi, sin, cos, sin, asin, acos, atan, atan2, sqrt, radians
import numpy as np
import time

#information detail Robot
L1 = 7
L2 = 10
L3 = 21

_a = [7.4, -26.75, 5.5]
a = np.array(_a)

def xinchao():
    x = 7.4
    y = -26.75
    a = atan(y/x)
    b = atan2(y,x)
    c = radians(90)
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)



def tempt(x, y , z):
    c =x + y + z
    round(c, 2)
    print(c)

def IK(x, y , z):
    try:
        f1 = pi - (-atan(y/x) + atan(sqrt(x**2 + y**2  - L1**2)/L1))
        f3 = acos((x**2 + y**2 + z**2 - L1**2 - L2**2 - L3**2)/(2*L2*L3))       
        theta_1 = degrees(f1)
        theta_3 = degrees(f3)
        f2 = atan(z/(sqrt(x**2 + y**2 + z**2 - L1**2))) - atan((L3*sin(radians(theta_3)))/(L2 + L3*cos(radians(theta_3))))
        theta_2 = degrees(f2)
        theta = [theta_1, theta_2, theta_3]
    except:
        print("Viet ham dua cac chan de robot 4 chan dung im")

    
    return(theta)

def Dangdi(t):
    if t == 1:
        print("ban chon kieu di crawl, chua viet")
    if t == 2:
        print("ban chon kieu di trot")
        Ditoi()
        

def Ditoi():
    # a la bien di toi di lui re trai re phai 
    a = int(input("Nhap 1: Di toi \ Nhap 2: Di lui "))
    if a == 1:
        print("Di toi")
        TM = float(input("Nhap chu ky TM = "))
        S = float(input("Nhap chu ky S = "))
        H = float(input("Nhap chu ky H = "))
        Vantoc_trot(TM, S, H, a)

def Vantoc_trot(TM, S, H, a):
    # do phan giai thoi gian 
    b = 0.1
    for t in np.arange(0, 2*TM, b):
        if (t < TM/2):
            time.sleep(0.1)
            print("dang o nua chi ki 1", t + b)
            Quydao_trot(TM, S, H, a)
        if (t >= TM/2 and t < TM):
            time.sleep(0.1)
            print("dang o nua chi ki 2", t + b)
        if (t  >= TM):
            time.sleep(0.1)
            print("dang o  chi ki di ve", t + b)

def Quydao_trot(TM, S, H, a):
    if (a == 1):
        print("a")