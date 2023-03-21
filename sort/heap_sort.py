def Heap_sort(arr):
    print("Build Max Heap Array: ", end="\n")
    Build_max_heap(arr)
    print_Arr(arr)
    
    for i in range(len(arr)-1, 0, -1):
        swap(arr, 1, i)
        Max_heapify(arr, 1)
def Build_max_heap(arr):
    for i in range((len(arr)-1)//2, 0,-1):
        Max_heapify(arr, i)
def Max_heapify(arr, i):
# L, R, i, largest為index
    L = Left(i)
    R = Right(i)
    if L < len(arr) and arr[L] > arr[i]: 
        largest = L
    else:
        largest = i
    if R < len(arr) and arr[R] > arr[largest]:
        largest = R
    if largest != i:
        swap(arr, i, largest)
        Max_heapify(arr, largest)  
    
def swap(arr, a, b):
    empty = arr[a]
    arr[a] = arr[b]
    arr[b] = empty
def Left(i):
    return 2*i
def Right(i):
    return 2*i+1

def print_Arr(arr):
    for i in range(1, len(arr)):
        print(arr[i], end=" ")
    print("\n")
 
if __name__ == '__main__':
    arr = [0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1] #heapify 只能從[1]開始 so set[0]=0
    print("Array: ", end="\n")
    print_Arr(arr)

    Heap_sort(arr)
    print("Heap Sort Array: ", end="\n")
    print_Arr(arr)