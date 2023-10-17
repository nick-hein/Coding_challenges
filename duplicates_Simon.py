import random

numbers = []
length = 1000
for num in range(length):
    numbers.append(random.randint(0,length+1))
def findDuplicates(nums):
  dups = 0
  pos = []
  totalDups = 0
  for num in range(length):
    for index, dup in enumerate(nums):
      if num == dup:
        dups = dups + 1
        pos.append(str(index))
    if dups >= 2:
      totalDups += 1
      print("Duplicate " + str(totalDups) + ": " + str(num) + "\nIn positions "+ str(", ".join(pos)) + "\n")
    dups = 0
    pos = []

  print(nums)
findDuplicates(numbers)