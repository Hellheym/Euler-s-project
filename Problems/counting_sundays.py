days = 365 * 100 + 25
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a = 1
year = 0
sunday_count = 0

while a <= days:
    year += 1
    if year % 4 != 0:
        for i in months:
            a += i
            if a % 7 == 6:
                sunday_count += 1
    else:
        for i in months:
            if i == 28:
                a += i+1
            else:
                a += i
            if a % 7 == 6:
                sunday_count += 1
print(sunday_count)