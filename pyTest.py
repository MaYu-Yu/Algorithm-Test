def fibo(k, x0=0, x1=1):
    if k <= 0:
        return x0
    if k == 1:
        return x1
    return fibo(k - 1, x1, x0+x1)
if __name__ == "__main__":
    for i in range(10):
        print(fibo(i), end=" ")