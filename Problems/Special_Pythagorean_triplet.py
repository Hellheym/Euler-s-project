def triplets():
    for i in range(1, 998):
        a = i
        for j in range(a+1, 999-a):
            b = j
            c = 1000 - (a + b)
            if (a**2) + (b**2) == (c**2):
                return a, b, c

triplet = triplets()
print(triplet)
product = triplet[0] * triplet[1] * triplet[2]
print(product)