# Eratosthenes sieve method 
def findPrime(n):
    isPrime = [True for _ in range(n)]
    for i in range(2, n):
        if isPrime[i] == True:
            print(i, end=' ')
            k = i*i
            while k < n:
                isPrime[k] = False             
                k+=i
if __name__ == "__main__":
    findPrime(100)