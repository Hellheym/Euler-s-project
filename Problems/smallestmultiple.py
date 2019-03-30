answer = 1
for i in range(1,21):
	a=1
	if answer%i != 0:
		while a<=20:
			a = i*a
		answer = answer * a / i
print(answer)