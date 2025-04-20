#import re
from functools import cmp_to_key
inp = []
inp2 = []
result = 0

with open("input.txt", "r") as f:
    second = False
    for line in f:
        if line.rstrip() == "":
            second = True
        elif not second:
            inp.append(line.rstrip())
        elif second:
            inp2.append(line.rstrip())

#Part 1
goodI = []
cons = {}
for con in inp:
    a, b = con.split("|")
    a = int(a)
    b = int(b)
    if b in cons:
        cons[b].append(a)
    else:
        cons[b] = [a]
for li in range(len(inp2)):
    l = inp2[li]
    goNext = False
    numl = [int(a) for a in l.split(",")]
    for i in range(len(numl)):
        num = numl[i]
        if goNext:
            break
        if num in cons:
            for pred in cons[num]:
                if pred in numl:
                    if numl.index(pred) > i:
                        goNext = True
                        break
    if not goNext:
        goodI.append(li)
        result = result + numl[len(numl)//2]

print(result)

#Part 2
result = 0
def conp(a,b):
    if b in cons[a]:
        return 1
    elif a in cons[b]:
        return -1
    else:
        return 0

for li in range(len(inp2)):
    if li in goodI:
        continue
    l = inp2[li]
    numl = [int(a) for a in l.split(",")]
    ## Redit help to use sort and conp function
    numl = sorted(numl, key=cmp_to_key(conp))
    result = result + numl[len(numl)//2]

print(result)

