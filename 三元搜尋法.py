from lib import swap

def ternarySearch(arr, l, r, target):
    if l > r:
        return -1
    if l == r: 
        if target == arr[l]:
            return l
        else:
            return -1
    if arr[l] > arr[r]: swap(arr, l, r)
    mid_1 = l
    pivot = arr[l]
    for i in range(l+1, r+1):
        if arr[i] < pivot: 
            mid_1+=1
            swap(arr, i, mid_1)
    swap(arr, mid_1, l)
    mid_2 = r
    pivot = arr[r]
    for i in range(r-1, mid_1, -1):
        if arr[i] > pivot: 
            mid_2-=1
            swap(arr, i, mid_2)
    swap(arr, mid_2, r)
    
    if target < arr[mid_1]:
        return ternarySearch(arr, l + 1, mid_1 - 1, target)
    elif target < arr[mid_2]:
        return ternarySearch(arr, mid_1 + 1, mid_2 - 1, target)
    elif target > arr[mid_2]:
        return ternarySearch(arr, mid_2 + 1, r - 1, target)
    else:
        if target == arr[mid_1]: 
            return mid_1
        else: 
            return mid_2
if __name__ == "__main__":
    arr = [69,75,28,76,7,15,53,34]
    target = 69
    print(ternarySearch(arr, 0, len(arr) - 1, target))
    print(arr)