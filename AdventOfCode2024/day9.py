#import re
#from functools import cmp_to_key
from copy import deepcopy
inp = ""
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp = line.rstrip()
#Part 1
nums = []
spaces = []
for i in range(0,len(inp), 2):
    nums.append(int(inp[i]))
    if (i+1 < len(inp)):
        spaces.append(int(inp[i+1]))

itSpaces = 0
itNumsFront = 0
itNumsBack = len(nums)-1

for i in range(sum(nums)):
    if spaces[itSpaces] == 0:
        itSpaces = itSpaces + 1
    if nums[itNumsFront] == 0:
        itNumsFront = itNumsFront + 1
    if nums[itNumsBack] == 0:
        itNumsBack = itNumsBack - 1
    if itNumsFront > itSpaces:
        spaces[itSpaces] = spaces[itSpaces] - 1
        nums[itNumsBack] = nums[itNumsBack] - 1
        result = result + i*itNumsBack
    else:
        nums[itNumsFront] = nums[itNumsFront] - 1
        result = result + i*itNumsFront

print(result)

#Part 2
result = 0

nums = []
for i in range(0,len(inp), 2):
    nums.append((i//2, int(inp[i])))
    if (i+1 < len(inp)):
        nums.append((-1, int(inp[i+1])))

for i in range(len(nums)-1, -1, -1):
    if (nums[i][0] == -1):
        continue
    for j in range(i):
        if (nums[j][0] != -1):
            continue
        if nums[i][1] <= nums[j][1]:
            nums[j] = (nums[j][0], nums[j][1] - nums[i][1])
            nums.insert(i, (-1, nums[i][1]))
            nums.insert(j, nums.pop(i+1))
            break

itNumsFront = 0
i = 0
while itNumsFront < len(nums):
    if nums[itNumsFront][1] == 0:
        itNumsFront = itNumsFront + 1
        continue
    
    nums[itNumsFront] = (nums[itNumsFront][0], nums[itNumsFront][1] - 1)
    if nums[itNumsFront][0] != -1:
        result = result + i*nums[itNumsFront][0]
    i = i + 1
print(result)

    
