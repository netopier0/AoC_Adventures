#import re
#from functools import cmp_to_key
inp = []
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

#Part 1
def isCorrect(exp, nums, curr):
    if len(nums) == 0:
        return exp == curr
    return isCorrect(exp, nums[1:], curr+nums[0]) or isCorrect(exp, nums[1:], curr*nums[0])

for l in inp:
    lspitted = l.split()
    exp = int(lspitted[0][:-1])
    nums = [int(x) for x in lspitted[1:]]
    if isCorrect(exp, nums[1:], nums[0]):
        result = result + exp

print(result)
    

#Part 2
result = 0

def isCorrectTwo(exp, nums, curr):
    if len(nums) == 0:
        return exp == curr
    return isCorrectTwo(exp, nums[1:], curr+nums[0]) or isCorrectTwo(exp, nums[1:], curr*nums[0]) or isCorrectTwo(exp, nums[1:], int(str(curr) + str(nums[0])))

for l in inp:
    lspitted = l.split()
    exp = int(lspitted[0][:-1])
    nums = [int(x) for x in lspitted[1:]]
    if isCorrectTwo(exp, nums[1:], nums[0]):
        result = result + exp

print(result)
