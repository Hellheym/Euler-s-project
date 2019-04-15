import math as m

amicable = []

for i in range(1, 10001):
    divsa = []
    divsb = []
    a = i
    if a in amicable:
        continue
    if int(m.sqrt(a))+1 >= 3:
        for j in range(1, int(m.sqrt(a))+1):
            if a % j == 0:
                divsa.append(j)
                if j > 1:
                    divsa.append(a // j)
    b = sum(divsa)
    if a == b:
        continue
    if int(m.sqrt(b))+1 >= 3:
        for j in range(1, int(m.sqrt(b))+1):
            if b % j == 0:
                divsb.append(j)
                if j > 1:
                    divsb.append(b // j)
    if sum(divsb) == a:
        amicable.extend((a, b))
print(amicable)
print(sum(amicable))