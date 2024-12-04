import math
a_13NTD = float(input("a = "))
b_13NTD = float(input("b = "))
c_13NTD = float(input("c = "))
print("{0}x^2 + {1}x + {2} = 0".format(a_13NTD, b_13NTD, c_13NTD))

if a_13NTD == 0: 
    print("Day khong phai phuong trinh bac hai")
else: 
    delta = math.pow(b_13NTD, 2) - 2*a_13NTD*c_13NTD
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b_13NTD/(2*a_13NTD)
        print("Phuong trinh co nghiem kep x = ", +str(x))
    else:
        x1 = (-b_13NTD-math.sqrt(delta))/(2*a_13NTD)
        x2 = (-b_13NTD+math.sqrt(delta))/(2*a_13NTD)
        print("Phuong trinh co 2 nghiem x1 = {0} va x2 = {1}".format(x1, x2))
