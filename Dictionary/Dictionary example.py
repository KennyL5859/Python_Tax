
classDict = {}

print(type(classDict))


classDict['CIS1400'] = 'Prog'
classDict['CIS2531'] = 'Intro to Python Prog'
classDict['CIS2532'] = 'Adv Python Prog'
classDict['CIS1400'] = 'Prog Logic and Technique'

print(classDict)
print()
print(classDict['CIS1400'])
print('CIS1400' in classDict)
print('CIS1299' in classDict)
print()

for i in classDict:
    print(i, end=' ')
print()

for i in classDict.values():
    print(i, end=' ')
print()

for i,k in classDict.items():   # Prints out the whole dictionary
    print(i, k)

# CIS1400 Prog Logic and Technique
# CIS2531 Intro to Python Prog
# CIS2532 Adv Python Prog


# del classDict['CIS1400']
print()

print(classDict.get('CIS2531', 'NOT FOUND'))  # Intro to Python Prog
print(classDict.get('CIS1450', 'NOT FOUND'))  # NOT FOUND
print()

myKeys = classDict.keys()
print(myKeys)   # dict_keys(['CIS1400', 'CIS2531', 'CIS2532'])
print()

print(classDict.pop('CIS1400', 'NOT FOUND'))
print(classDict.pop('CIS2531', 'NOT FOUND'))

print()

classDict.clear()
print(len(classDict))

import platform

print(platform.python_implementation())
print(platform.python_build())
print(platform.python_version())









