#import re
#from functools import cache, cmp_to_key
#from copy import deepcopy
from collections import deque

inp = []
result = 0
steps = []

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())
        steps.append(len(inp[-1]) * [-1])

sX = 0
sY = 0
eX = 0
eY = 0

for i in range(len(inp)):
    if "S" in inp[i]:
        sX = inp[i].index("S")
        sY = i
    if "E" in inp[i]:
        eX = inp[i].index("E")
        eY = i    
#Part 1
q = deque()
q.append((sY, sX, 0))
seen = set()
while len(q) > 0:
    y, x, score = q.popleft()

    if (x,y) in seen:
        continue
    
    seen.add((x,y))

    if inp[y][x] == '#':
        continue

    steps[y][x] = score

    q.append((y-1, x, score+1))
    q.append((y+1, x, score+1))
    q.append((y, x-1, score+1))
    q.append((y, x+1, score+1))


q = deque()
q.append((sY, sX))
seen = set()
allCheat = []
while len(q) > 0:
    y, x = q.popleft()

    if (x,y) in seen:
        continue
    
    seen.add((x,y))

    if inp[y][x] == '#':
        continue

    if y > 1:
        if steps[y][x] + 2 < steps[y-2][x]:
            allCheat.append(steps[y-2][x] - (steps[y][x] + 2))
    if y < len(inp)-2:
        if steps[y][x] + 2 < steps[y+2][x]:
            allCheat.append(steps[y+2][x] - (steps[y][x] + 2))
    if x > 1:
        if steps[y][x] + 2 < steps[y][x-2]:
            allCheat.append(steps[y][x-2] - (steps[y][x] + 2))
    if x < len(inp[y])-2:
        if steps[y][x] + 2 < steps[y][x+2]:
            allCheat.append(steps[y][x+2] - (steps[y][x] + 2))

    q.append((y-1, x))
    q.append((y+1, x))
    q.append((y, x-1))
    q.append((y, x+1))

result = len(list(filter(lambda x: x >= 100, allCheat)))
print(result)

#Part 2
q = deque()
q.append((sY, sX))
seen = set()
result = 0
while len(q) > 0:
    y, x = q.popleft()

    if (x,y) in seen:
        continue
    
    seen.add((x,y))

    if inp[y][x] == '#':
        continue

    for j in range(-20, 21):
        for k in range(-20, 21):
            if abs(j) + abs(k) < 21 and 0 <= y+j and y+j < len(inp) and 0 <= x+k and  x+k < len(inp[y]):
                if steps[y+j][x+k] - (steps[y][x] + abs(j) + abs(k)) >= 100:
                    result += 1

    q.append((y-1, x))
    q.append((y+1, x))
    q.append((y, x-1))
    q.append((y, x+1))

print(result)
