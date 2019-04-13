# Realization of my second solution by skdf1020
# (This idea comes to me just before i get the solution in my first try)
# P.S. it's a bit more than 1 sec that you wrote in Euler forum (or my comp is just piece of scrap)

record2 = 0
a = {}
for i in range(0, 1000000):
	count = 0
	x = i
	while x > 1:
		if x in a:
			count += a[x]
			break
		else:
			if x%2 == 0: x /= 2
			else: x = x*3 + 1
			count += 1
	a[i] = count
	if count > record2:
		record2 = count
		z = i
print(z)

# My first simple bruteforce solution
# import time
#
# start = time.time()
#
# maxchain = 0
# result = 0
#
# for i in range(2, 1000000+1):
#     chain = 1
#     number = i
#     while number != 1:
#         if number % 2 == 0:
#             number = number // 2
#             chain += 1
#             continue
#         if number % 2 == 1:
#             number = 3 * number + 1
#             chain += 1
#             continue
#     if chain > maxchain:
#         maxchain = chain
#         result = i
#
# end = time.time()
# print(maxchain)
# print(result)
# print(end - start)