def fastexp(x,n):
    p = 1
    while(n > 0):
        if n & 1:
            p*=x
        x*=x
        n >>= 1
    return p
if __name__ == "__main__":
    print(fastexp(2, 13))