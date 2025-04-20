#import re
#from functools import cmp_to_key
#from copy import deepcopy

inp = []
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

#Part 1
quads = [0, 0, 0, 0]

for l in inp:
    startX = int(l[l.index("=")+1:l.index(",")])
    startY = int(l[l.index(",")+1:l.index(" ")])
    lsec = l[l.index(" "):]
    X = int(lsec[lsec.index("=")+1:lsec.index(",")])
    Y = int(lsec[lsec.index(",")+1:])
    startX = (startX + X * 100)%101
    startY = (startY + Y * 100)%103
    if startX < 50 and startY < 51:
        quads[0] += 1
    elif startX > 50 and startY < 51:
        quads[1] += 1
    elif startX < 50 and startY > 51:
        quads[2] += 1
    elif startX > 50 and startY > 51:
        quads[3] += 1
result = quads[0] * quads[1] * quads[2] * quads[3]

print(result)

#Part 2
pos = []
mov = []
for l in inp:
    pos.append((int(l[l.index("=")+1:l.index(",")]), int(l[l.index(",")+1:l.index(" ")])))
    lsec = l[l.index(" "):]
    mov.append((int(lsec[lsec.index("=")+1:lsec.index(",")]), int(lsec[lsec.index(",")+1:])))

def drawPos():
    res = ""
    for i in range(105):
        for j in range(105):
            if (j, i) in pos:
                res = res + "X"
            else:
                res = res + " "
        res = res + "\n"
    print(res)

def step():
    for i in range(len(pos)):
        pos[i] = ((pos[i][0]+mov[i][0])%101, (pos[i][1]+mov[i][1])%103)

#Help from reddit to see what the tree should look like
counter = 0
while counter > -1:
    step()
    counter += 1
    for i in range(103):
        if len(list(filter(lambda x: x[0] == i, pos))) > 30:
            for j in range(103):
                if len(list(filter(lambda x: x[1] == j, pos))) > 30:
                    print(counter)
                    drawPos()
                    counter = -1
                    break
