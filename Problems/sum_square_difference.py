def sumofsquares(x):
    a = 0
    for i in range(1, x+1):
        a += i**2
    return a

def squareofsum(y):
    b = 0
    for i in range(1, y+1):
        b += i
    return b**2

z = 100
print(squareofsum(z) - sumofsquares(z))