import itertools

def prime(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True

primes = []
while len(primes) < 10001:
    for i in itertools.count():
        if prime(i):
            primes.append(i)
        if len(primes) == 10001:
            break
print(primes[-1])
# very long code