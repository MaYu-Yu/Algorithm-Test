def exp(n, a):
    if n > 1:
        x = exp(n//2, a)
        return x*x
    else:
        return a
if __name__ == "__main__":
    print(exp(4,3))