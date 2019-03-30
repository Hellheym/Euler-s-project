def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

n = 600851475143
factors = []
while n != 1:
    for i in range(2, isqrt(n)):
        if n % i == 0:
            factors.append(i)
            n /= i
            continue
print(factors)
print("Максимальный простой делитель = " + str(max(factors)))