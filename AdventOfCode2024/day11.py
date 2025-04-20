#import re
#from functools import cmp_to_key

inp = []
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

#Part 1
stones = inp[0].split()

def step(curr):
    result = []
    for s in curr:
        if s == '0':
            result.append('1')
        elif len(s)%2 == 0:
            result.append(str(int(s[:len(s)//2])))
            result.append(str(int(s[len(s)//2:])))
        else:
            result.append(str(int(s)*2024))
    return result

for i in range(25):
    stones = step(stones)

result = len(stones)
print(result)

#Part 2
stonesDict = {}
for s in inp[0].split():
    if s in stonesDict:
        stonesDict[s] += 1
    else:
        stonesDict[s] = 1


def stepDict(curr):
    result = {}
    for s in curr.keys():
        if s == '0':
            if '1' in result:
                result['1'] += curr[s]
            else:
                result['1'] = curr[s]
        elif len(s)%2 == 0:
            half = str(int(s[:len(s)//2]))
            if half in result:
                result[half] += curr[s]
            else:
                result[half] = curr[s]
            
            half = str(int(s[len(s)//2:]))
            if half in result:
                result[half] += curr[s]
            else:
                result[half] = curr[s]
        else:
            mult = str(int(s)*2024)
            if mult in result:
                result[mult] += curr[s]
            else:
                result[mult] = curr[s]
    return result

for i in range(75):
    stonesDict = stepDict(stonesDict)

result = 0
for s in stonesDict.keys():
    result += stonesDict[s]

print(result)
