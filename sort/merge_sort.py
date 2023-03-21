def merge_sort(arr):
    if len(arr) > 1:
    #瘋狂砍半
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
    #大小排序，小的在左
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    #左右不對稱時do it
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def print_Arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("\n")
 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Array: ", end="\n")
    print_Arr(arr)
    merge_sort(arr)
    print("Merge Sorted Array: ", end="\n")
    print_Arr(arr)