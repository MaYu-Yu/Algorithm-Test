def comb(n, m):
    a = [1 for _ in range(m + 1)]
    for i in range(n - m): 
        for j in range(1, m + 1):
            a[j] = a[j] + a[j - 1]
    return a[m]
def comb_r(n, m):
    if m == 0 or n == m: return 1
    return comb_r(n-1, m) + comb_r(n-1, m-1)
if __name__ == "__main__":
    print(comb(5,3))
    print(comb_r(5,3))