def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(40) / (factorial(20) * factorial(40-20))
print(result)