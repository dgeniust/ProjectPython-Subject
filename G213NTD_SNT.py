#Sàng số nguyên tố
import math
SNT_13NguyenThanhDat = [True] * 100

def SNT_13NTD():
    SNT_13NguyenThanhDat[0] = SNT_13NguyenThanhDat[1] = False
    for i in range(2, int(math.sqrt(100))):
        if SNT_13NguyenThanhDat[i]:
            for j in range(i*i, 100, i):
                SNT_13NguyenThanhDat[j] = False
def main():
    SNT_13NTD()
    for i in range(100):
        if SNT_13NguyenThanhDat[i] == True:
            print(i)
main()