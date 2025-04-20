#import re
#from functools import cmp_to_key
#from copy import deepcopy

inp = []
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

#Part 1
        
for lInd in range((len(inp)+1)//4):
    ButA=inp[4*lInd]
    aX = int(ButA[ButA.index("+")+1:ButA.index(",")])
    aY = int(ButA[ButA.index(",")+4:])
    ButB=inp[4*lInd+1]
    bX = int(ButB[ButB.index("+")+1:ButB.index(",")])
    bY = int(ButB[ButB.index(",")+4:])
    Res=inp[4*lInd+2]
    rX = int(Res[Res.index("=")+1:Res.index(",")])
    rY = int(Res[Res.index(",")+4:])

    curLow = 100000
    for a in range(100):
        for b in range(100):
            if a*aX + b*bX == rX and a*aY + b*bY == rY:
                curLow = min(curLow, a*3+b)
    if curLow < 100000:
        result = result + curLow

print(result)

#Part 2
result = 0

# Cramer's rule
def cramer(a, b, c):
    det = a[0]*b[1]-b[0]*a[1]
    x = (c[0]*b[1]-b[0]*c[1])//det
    y = (a[0]*c[1]-c[0]*a[1])//det
    if (c[0]*b[1]-b[0]*c[1])%det == 0 or (a[0]*c[1]-c[0]*a[1])//det == 0:
        return (x, y)
    return False

for lInd in range((len(inp)+1)//4):
    ButA=inp[4*lInd]
    a = (int(ButA[ButA.index("+")+1:ButA.index(",")]), int(ButA[ButA.index(",")+4:]))
    ButB=inp[4*lInd+1]
    b = (int(ButB[ButB.index("+")+1:ButB.index(",")]), int(ButB[ButB.index(",")+4:]))
    Res=inp[4*lInd+2]
    r= (int(Res[Res.index("=")+1:Res.index(",")]) + 10000000000000, int(Res[Res.index(",")+4:]) + 10000000000000)

    craRes = cramer(a, b, r)
    if craRes:
        result = result + craRes[0]*3+craRes[1]

print(result)
