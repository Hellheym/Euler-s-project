with open("p022_names.txt", "r") as f:
    a = f.read()
a = a.replace('"', '').split(',')
a.sort()

alphabet = list(map(chr, range(65, 91)))
total = 0

for i in a:
    value = 0
    for j in i:
        value += alphabet.index(j) + 1
    position = a.index(i) + 1
    total += (position * value)
print(total)


# with open('p022_names.txt','r') as f: s = f.read()
#
# l = s.replace('"','').split(",")
# l.sort()
#
# for i in range(len(l)):
#     l[i] = sum([ord(c)-64 for c in l[i]]) * (i + 1)
#
# print(sum(l))