def insert_sort(arr):
    for j in range(1, len(arr)):
        k = arr[j]
        i = j-1
    #比抽到的牌還大就往前推一格
        while i>=0 and arr[i]>k:
            arr[i+1] = arr[i]
            i-=1
    #插入牌
        arr[i+1] = k

def print_Arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("\n")
 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Array: ", end="\n")
    print_Arr(arr)
    insert_sort(arr)
    print("Insert Sorted Array: ", end="\n")
    print_Arr(arr)