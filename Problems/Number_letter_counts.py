import inflect
p = inflect.engine()

allletters = ''

for i in range(1, 1000+1):
    a = p.number_to_words(i)
    a = a.replace(' ', '')
    a = a.replace('-', '')
    allletters += a
print(len(allletters))