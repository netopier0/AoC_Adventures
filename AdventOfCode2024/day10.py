#import re
#from functools import cmp_to_key

inp = []
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

#Part 1
starts = []
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == '0':
            starts.append((i,j))


def scaleStep(y, x):
    curr = int(inp[y][x])
    if curr == 9:
        return [(y, x)]
    result = []
    if y > 0 and int(inp[y-1][x]) == curr+1:
        result = result + scaleStep(y-1, x)
    if y < len(inp)-1 and int(inp[y+1][x]) == curr+1:
        result = result + scaleStep(y+1, x)
    if x > 0 and int(inp[y][x-1]) == curr+1:
        result = result + scaleStep(y, x-1)
    if x < len(inp[y])-1 and int(inp[y][x+1]) == curr+1:
        result = result + scaleStep(y, x+1)
    return result

for y, x in starts:
    result = result + len(set(scaleStep(y,x)))

print(result)

#Part 2
result = 0

for y, x in starts:
    result = result + len(scaleStep(y,x))

print(result)
