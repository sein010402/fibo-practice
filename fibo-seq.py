def fibo(n):
    if n < 2:
        return n
    else:
        fibo(n - 1) + fibo(n - 2)
