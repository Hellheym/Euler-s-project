n = 1
x = 0
for i in range(1, 101):
    n *= i
n = str(n)

for i in n:
    x += int(i)
print(x)