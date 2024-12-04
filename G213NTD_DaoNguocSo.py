#Đảo ngược số 
def G13NTD_DaoNguocSo(n): 
    m = 0
    while n != 0:
        m = m*10 + (n%10)
        n //= 10
    return m
def main():
    m = int(input("Nhap so n: "))
    print(G13NTD_DaoNguocSo(m))
main()    