#import re
#from functools import cmp_to_key
#from copy import deepcopy
from collections import deque

inp = []
result = []

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

#Part 1
for i in range(71):
    result.append([-1] * 71)

walls = []
for i in range(1024):
    walls.append((int(inp[i][:inp[i].index(",")]), int(inp[i][inp[i].index(",")+1:])))

q = deque()
q.append((0,0,0))
seen = set()
while len(q) > 0:
    y, x, score = q.popleft()

    if (x,y) in seen:
        continue
    
    seen.add((x,y))
    
    if (x,y) in walls:
        continue

    result[y][x] = score

    if y > 0:
        q.append((y-1, x, score+1))
    if y < 70:
        q.append((y+1, x, score+1))
    if x > 0:
        q.append((y, x-1, score+1))
    if x < 70:
        q.append((y, x+1, score+1))

print(result[70][70])

#Part 2
walls = []
for i in range(len(inp)):
    walls.append((int(inp[i][:inp[i].index(",")]), int(inp[i][inp[i].index(",")+1:])))

binMin = 0
binMax = len(inp)
while binMin < binMax:
    mid = (binMin + binMax)//2

    result = []
    for i in range(71):
        result.append([-1] * 71)

    q = deque()
    q.append((0,0,0))
    seen = set()
    while len(q) > 0:
        y, x, score = q.popleft()

        if (x,y) in seen:
            continue
    
        seen.add((x,y))
    
        if (x,y) in walls[:mid]:
            continue

        result[y][x] = score

        if y > 0:
            q.append((y-1, x, score+1))
        if y < 70:
            q.append((y+1, x, score+1))
        if x > 0:
            q.append((y, x-1, score+1))
        if x < 70:
            q.append((y, x+1, score+1))

    if result[70][70] == -1:
        binMax = mid-1
    else:
        binMin = mid+1
            
result = inp[(binMin + binMax)//2-1]
print(result)
