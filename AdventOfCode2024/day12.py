#import re
#from functools import cmp_to_key
from copy import deepcopy
inp = []
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

origInp = deepcopy(inp)

def repl(s, c, pos):
    return s[:pos] + c + s[pos+1:]

#Part 1
def traversePlot(y, x):
    curr = inp[y][x]
    if curr == '.':
        return (0, 0)
    inp[y] = repl(inp[y], '.', x)
    s = 1
    l = 0

    if y > 0 and inp[y-1][x] == curr:
        r = traversePlot(y-1, x)
        s = s + r[0]
        l = l + r[1]
    elif y == 0 or origInp[y-1][x] != curr:
        l = l + 1
        
    if y < len(inp)-1 and inp[y+1][x] == curr:
        r = traversePlot(y+1, x)
        s = s + r[0]
        l = l + r[1]
    elif y == len(inp)-1 or origInp[y+1][x] != curr:
        l = l + 1

    if x > 0 and inp[y][x-1] == curr:
        r = traversePlot(y, x-1)
        s = s + r[0]
        l = l + r[1]
    elif x == 0 or origInp[y][x-1] != curr:
        l = l + 1
        
    if x < len(inp[y])-1 and inp[y][x+1] == curr:
        r = traversePlot(y, x+1)
        s = s + r[0]
        l = l + r[1]
    elif x == len(inp[y])-1 or origInp[y][x+1] != curr:
        l = l + 1

    return (s ,l)
    

    

for y in range(len(inp)):
    for x in range(len(inp[y])):
        if inp[y][x] == '.':
            continue
        r = traversePlot(y, x)
        result = result + r[0]*r[1]


print(result)


#Part 2
result = 0

def getWalls(y, x):
    curr = origInp[y][x]
    cont = []
    cont.append(y != 0 and origInp[y-1][x] == curr) #UP
    cont.append(y != len(inp)-1 and origInp[y+1][x] == curr) #DOWN
    cont.append(x != 0 and origInp[y][x-1] == curr) #Left
    cont.append(x != len(inp[y])-1 and origInp[y][x+1] == curr) #Right

    #Smart from reddit: Number of corners = number of walls
    
    #Zero
    if cont.count(False) == 4:
        return 4
    
    #One
    if cont.count(False) == 3:
        return 2
    
    #Two Stright
    if cont[0] and cont[1] and not cont[2] and not cont[3]:
        return 0
    if not cont[0] and not cont[1] and cont[2] and cont[3]:
        return 0
    
    #Two Turn
    if cont[0] and not cont[1] and not cont[2] and cont[3]:
        if y == 0 or x == len(inp[y])-1:
            return 1
        if origInp[y-1][x+1] != curr:
            return 2
        return 1
    if cont[0] and not cont[1] and cont[2] and not cont[3]:
        if y == 0 or x == 0:
            return 1
        if origInp[y-1][x-1] != curr:
            return 2
        return 1
    if not cont[0] and cont[1] and not cont[2] and cont[3]:
        if y == len(inp)-1 or x == len(inp[y])-1:
            return 1
        if origInp[y+1][x+1] != curr:
            return 2
        return 1
    if not cont[0] and cont[1] and cont[2] and not cont[3]:
        if y == len(inp)-1 or x == 0:
            return 1
        if origInp[y+1][x-1] != curr:
            return 2
        return 1

    # Three
    if cont.count(False) == 1:
        r = 0
        if not cont[0]:
            if origInp[y+1][x+1] != curr:
                r = r + 1
            if origInp[y+1][x-1] != curr:
                r = r + 1
                
        if not cont[1]:
            if origInp[y-1][x+1] != curr:
                r = r + 1
            if origInp[y-1][x-1] != curr:
                r = r + 1

        if not cont[2]:
            if origInp[y-1][x+1] != curr:
                r = r + 1
            if origInp[y+1][x+1] != curr:
                r = r + 1

        if not cont[3]:
            if origInp[y-1][x-1] != curr:
                r = r + 1
            if origInp[y+1][x-1] != curr:
                r = r + 1
        return r

    # Four
    if cont.count(False) == 0:
        ret = 0
        if origInp[y-1][x+1] != curr:
            ret +=1
            
        if origInp[y-1][x-1] != curr:
            ret += 1

        if origInp[y+1][x+1] != curr:
            ret += 1

        if origInp[y+1][x-1] != curr:
            ret += 1
        return ret
    print("ERR")
    return 0
  

def traversePlotCor(y, x):
    curr = inp[y][x]
    if curr == '.':
        return (0, 0)
    inp[y] = repl(inp[y], '.', x)
    s = 1
    w = getWalls(y, x)
    
    if y > 0 and inp[y-1][x] == curr:
        r = traversePlotCor(y-1, x)
        s = s + r[0]
        w = w + r[1]
        
    if y < len(inp)-1 and inp[y+1][x] == curr:
        r = traversePlotCor(y+1, x)
        s = s + r[0]
        w = w + r[1]

    if x > 0 and inp[y][x-1] == curr:
        r = traversePlotCor(y, x-1)
        s = s + r[0]
        w = w + r[1]
        
    if x < len(inp[y])-1 and inp[y][x+1] == curr:
        r = traversePlotCor(y, x+1)
        s = s + r[0]
        w = w + r[1]
    return (s, w)
    

inp = deepcopy(origInp)

for y in range(len(inp)):
    for x in range(len(inp[y])):
        if inp[y][x] == '.':
            continue
        r = traversePlotCor(y, x)
        result = result + r[0]*r[1]

print(result)

