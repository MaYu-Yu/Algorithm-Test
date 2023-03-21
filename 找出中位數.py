from lib import swap
def partition(arr, l, r):
    pivot = arr[l]
    j = l
    for i in range(l+1, r+1):
        if arr[i] < pivot:
            j+=1
            swap(arr, i, j)
    swap(arr, l, j)
    return j
def findMean(arr):
    l, r = 0, len(arr) - 1
    mid_index = len(arr) // 2
    while l <= r:
        mid = partition(arr, l, r)
        if mid == mid_index:
            return arr[mid]
        if mid < mid_index:
            l = mid + 1
        else:
            r = mid - 1
    return -1
if __name__ == "__main__":
    arr = [69,75,28,76,7,15,53,34]
    print(findMean(arr))
    print(arr)