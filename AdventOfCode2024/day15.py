#import re
#from functools import cmp_to_key
from copy import deepcopy

inp = []
comm = ""
result = 0

with open("input.txt", "r") as f:
    inpLoaded = False
    for line in f:
        if line.rstrip() == "":
            inpLoaded = True
        if not inpLoaded:
            inp.append(line.rstrip())
        else:
            comm += line.rstrip()
origInp = deepcopy(inp)

#Part 1
y = 0
x = 0
for i in range(len(inp)):
    if "@" in inp[i]:
        y = i
        x = inp[i].index("@")

def changeStr(s, i, ch):
    return s[:i] + ch + s[i+1:]
    

def swap(s1, i1, s2, i2):
    if s2 is None:
        tmp = s1[i1]
        s1 = changeStr(s1, i1, s1[i2])
        s1 = changeStr(s1, i2, tmp)
        return s1
    tmp = s1[i1]
    s1 = changeStr(s1, i1, s2[i2])
    s2 = changeStr(s2, i2, tmp)
    return s1, s2

def nextSpace(y, x, dy, dx):
    counter = 0
    while inp[y][x] != ".":
        if inp[y][x] == "#":
            return -1
        y += dy
        x += dx
        counter += 1
    return counter


for d in comm:
    dy = 0
    dx = 0
    if d == "^":
        dy = -1
    elif d == "v":
        dy = 1
    elif d == "<":
        dx = -1
    elif d == ">":
        dx = 1

    space = nextSpace(y, x, dy, dx)
    if space == -1:
        continue
    y = y + dy*space
    x = x + dx*space
    if dy == 0:
        for i in range(space):
            inp[y] = swap(inp[y], x, None, x-dx)
            x -= dx
    else:
        for i in range(space):
            inp[y], inp[y-dy] = swap(inp[y], x, inp[y-dy], x)
            y -= dy
    y = y + dy
    x = x + dx

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == "O":
            result = result + 100*i + j
print(result)
            
#Part 2
result = 0
inp = deepcopy(origInp)

def moveY(y, x, dy):
    if inp[y+dy][x] == ".":
        return ([], True)
    if inp[y+dy][x] == "#":
        return ([], False)
    if inp[y+dy][x] == "[":
        a = moveY(y+dy, x, dy)
        b = moveY(y+dy, x+1, dy)
        if a[1] and b[1]:
            res = [(y+dy, x)]
            res += a[0]
            res += b[0]
            return (res, True)
        return ([], False)
    if inp[y+dy][x] == "]":
        a = moveY(y+dy, x-1, dy)
        b = moveY(y+dy, x, dy)
        if a[1] and b[1]:
            res = [(y+dy, x-1)]
            res += a[0]
            res += b[0]
            return (res, True)
        return ([], False)

for i in range(len(inp)):
    inp[i] = inp[i].replace("#", "##")
    inp[i] = inp[i].replace("O", "[]")
    inp[i] = inp[i].replace(".", "..")
    inp[i] = inp[i].replace("@", "@.")

for i in range(len(inp)):
    if "@" in inp[i]:
        y = i
        x = inp[i].index("@")

for d in comm:
    dy = 0
    dx = 0
    if d == "^":
        dy = -1
    elif d == "v":
        dy = 1
    elif d == "<":
        dx = -1
    elif d == ">":
        dx = 1
        
    if dy == 0:
        space = nextSpace(y, x, 0, dx)
        if space == -1:
            continue
        x = x + dx*space
        if dy == 0:
            for i in range(space):
                inp[y] = swap(inp[y], x, None, x-dx)
                x -= dx
        x = x + dx

    else:
        m = moveY(y, x, dy)
        if not m[1]:
            continue
        moveOrder = list(set(m[0]))
        if dy < 0:
            moveOrder = sorted(moveOrder, key=lambda x:x[0], reverse=False)
        else:
            moveOrder = sorted(moveOrder, key=lambda x:x[0], reverse=True)
        for el in moveOrder:
            inp[el[0]], inp[el[0]+dy] = swap(inp[el[0]], el[1], inp[el[0]+dy], el[1])
            inp[el[0]], inp[el[0]+dy] = swap(inp[el[0]], el[1]+1, inp[el[0]+dy], el[1]+1)
        inp[y], inp[y+dy] = swap(inp[y], x, inp[y+dy], x)
        y = y+dy

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == "[":
            result = result + 100*i + j
print(result)
        
