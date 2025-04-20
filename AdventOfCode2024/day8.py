#import re
#from functools import cmp_to_key
inp = []
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

antenaPos = {}
signalPos = []

def mulTuples(a, k):
    return (a[0]*k, a[1]*k)

def addTuples(a,b):
    return (a[0]+b[0],a[1]+b[1])

for y in range(len(inp)):
    for x in range(len(inp[y])):
        if inp[y][x] != ".":
            if inp[y][x] in antenaPos:
                antenaPos[inp[y][x]].append((y,x))
            else:
                antenaPos[inp[y][x]] = [(y,x)]
#Part 1
for k in antenaPos:
    for i in range(len(antenaPos[k])):
        for j in range(i+1, len(antenaPos[k])):
            a = antenaPos[k][i]
            b = antenaPos[k][j]
            res = addTuples(mulTuples(a, 2), mulTuples(b, -1))
            if res[0] >= 0 and res[0] < len(inp) and res[1] >= 0 and res[1] < len(inp[res[0]]):
                signalPos.append(res)
                
            res = addTuples(mulTuples(b, 2), mulTuples(a, -1))
            if res[0] >= 0 and res[0] < len(inp) and res[1] >= 0 and res[1] < len(inp[res[0]]):
                signalPos.append(res)

print(len(set(signalPos)))


#Part 2
signalPos = []
for k in antenaPos:
    for i in range(len(antenaPos[k])):
        for j in range(i+1, len(antenaPos[k])):
            a = antenaPos[k][i]
            b = antenaPos[k][j]
            dif = addTuples(a, mulTuples(b, -1))
            res = addTuples(b, dif)
            while res[0] >= 0 and res[0] < len(inp) and res[1] >= 0 and res[1] < len(inp[res[0]]):
                signalPos.append(res)
                res = addTuples(res, dif)
                
            dif = addTuples(b, mulTuples(a, -1))
            res = addTuples(a, dif)
            while res[0] >= 0 and res[0] < len(inp) and res[1] >= 0 and res[1] < len(inp[res[0]]):
                signalPos.append(res)
                res = addTuples(res, dif)

print(len(set(signalPos)))
