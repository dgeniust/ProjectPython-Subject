def HNT_13NguyenThanhDat(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    HNT_13NguyenThanhDat(n-1, source, auxiliary, destination)
    print ("Move disk+",n,"+from source",source,"to destination",destination)
    HNT_13NguyenThanhDat(n-1, auxiliary, destination, source)
        
# Driver code
def main():
    n = int(input("Hay chon so vong ma ban muon: "))
    HNT_13NguyenThanhDat(n,'A','B','C')
if __name__ == "__main__":
    main()