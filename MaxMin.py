def findMaxMin(a):
    if len(a) == 1: return a[0], a[0]
    else:
        mid = len(a) // 2
        lmin, lmax = findMaxMin(a[:mid])
        rmin, rmax = findMaxMin(a[mid:])
        return min(lmin, rmin), max(lmax, rmax)
def sos(a, n, m):
    if m == 0: 
        return 1
    elif m < 0 or n <= 0: 
        return 0
    else:
        return sos(a, n - 1, m) or sos(a, n - 1, m - a[n - 1])
if __name__ == "__main__":
    a = [32, 59, 17, 74, 28, 35, 8, 9 ]
    print(findMaxMin(a))
    print(sos(a, len(a), 74+17))