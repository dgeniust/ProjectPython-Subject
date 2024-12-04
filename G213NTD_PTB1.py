a_13NTD = float(input("a = "))
b_13NTD = float(input("b = "))
print("{0}x + {1} = 0".format(a_13NTD, b_13NTD))

if a_13NTD == 0 and b_13NTD == 0:
    print("Phuong trinh vo so nghiem")
elif a_13NTD == 0 and b_13NTD != 0:
    print("Phuong trinh vo nghiem")
else: 
    x_13NTD = -b_13NTD/a_13NTD
    print("Nghiem cua phuong trinh la " + str(x_13NTD))
