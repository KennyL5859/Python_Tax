
cis1400set = {'Ken', 'Joe', 'Kim', 'Mike', 'Johnson', 'Frank', 'Courtney'}

print(type(cis1400set))
print(len(cis1400set))
print()

for item in cis1400set:
    print(item)

print()
cis1400set.add('Star')
print(len(cis1400set))

print()
cis1400set.remove('Mike')
print(len(cis1400set))

print()
cis1400set.discard('Joe')
print(len(cis1400set))

print('Ken' in cis1400set)
print('Ken' not in cis1400set)


cis1450set = {'Jessica', 'Rick', 'Ken'}

print(cis1400set | cis1450set)  # {'Jessica', 'Johnson', 'Rick', 'Star', 'Kim', 'Frank', 'Ken', 'Courtney'}

allStudents = cis1450set.union(cis1400set)
print(allStudents)  # {'Jessica', 'Johnson', 'Rick', 'Star', 'Kim', 'Frank', 'Ken', 'Courtney'}


interStudents = cis1400set & cis1450set
print(interStudents)  # "Ken" (student that occurs in both set)

print()
print(cis1400set.difference(cis1450set))  # {'Frank', 'Johnson', 'Star', 'Kim', 'Courtney'}
print(cis1450set.difference(cis1400set))  # {'Jessica', 'Rick'}

print()

print(cis1400set.symmetric_difference(cis1450set))  # {'Star', 'Johnson', 'Rick', 'Frank', 'Jessica', 'Courtney', 'Kim'}
print(cis1450set.symmetric_difference(cis1400set))  # {'Frank', 'Rick', 'Star', 'Jessica', 'Courtney', 'Kim', 'Johnson'}

print()

studentSet = {'Joe', 'Ken', 'Carol'}
workerSet = {'Carol'}

print(workerSet <= studentSet)
print(studentSet <= workerSet)


cards = ('Jack', 'Queen', 'King', 'Ace', 'Carolyn')
values = (11, 12, 13, 1, 5)
print()

for c, v in zip(cards, values):
    print('{:>10} {:>5}'.format(c,v))

listValues = [11, 2, 13, 1, 6]

print()
for c, v in zip(cards, listValues):
    print('{:^10} {:^5}'.format(c,v))

def strToUpper(x):
    return str(x).upper()

print()
for each in map(strToUpper, cards):
    print(each)

# JACK
# QUEEN
# KING
# ACE
# CAROLYN





