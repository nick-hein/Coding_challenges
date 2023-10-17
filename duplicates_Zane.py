import random
list = []
duplicates = []
original = []

for i in range(0,10):
    list.append(random.randint(0,10))

def duplicates(numbers):
    original = []
    duplicates = []
    for i in numbers:
        if i not in original:
            original.append(i)
        elif i in original:
            duplicates.append(i)
    print(duplicates)
    print(original)
    print(numbers)

duplicates(list)