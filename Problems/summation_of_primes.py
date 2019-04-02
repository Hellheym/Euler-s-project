mylist = list(range(2000001))
mylist[1] = 0

for i in mylist:
  if i > 1:
    for j in range(i+i, len(mylist), i):
      mylist[j] = 0
mylist = list(filter(lambda x: x>0 , mylist))

print(sum(mylist))