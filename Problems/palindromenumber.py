def palindrome(number):
    listed_number = []
    for i in str(number):
        listed_number += [i]
    reversed_number = listed_number[::-1]
    return int(''.join(reversed_number))

list_of_palindromes = []

for i in range(1000, 100, -1):
    for y in range(i, 100, -1):
        number = i * y
        if number == palindrome(number):
            list_of_palindromes.append(number)
            if number == max(list_of_palindromes):
                mi = i
                my = y
        else:
            continue
list_of_palindromes.sort()
print(str(max(list_of_palindromes)) + ', multipliers are ' + str(mi) + ' and ' + str(my))