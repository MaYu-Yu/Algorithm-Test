def printArr(arr):
    m,n = len(arr), len(arr[0])
    for i in range(m):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
def lowerTriangularArr(m, n):
    arr = [ [0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i >= j:
                arr[i][j] = 1 
    print("下三角矩陣: ")
    printArr(arr)
def upperTriangularArr(m, n):
    arr = [ [0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i <= j:
                arr[i][j] = 1 
    print("上三角矩陣: ")
    printArr(arr)
if __name__ == "__main__":
    m, n = 6, 6
    lowerTriangularArr(m, n)
    upperTriangularArr(m, n)
    
