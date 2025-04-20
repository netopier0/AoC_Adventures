#import re
#from functools import cmp_to_key
inp = []
result = 0

#Part 1
with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

posy = -1
posx = -1
currentSymbol = "^"
for i in range(len(inp)):
    if "^" in inp[i]:
        posy = i
        posx = inp[i].index("^")

def change(s, pos, ch):
    return s[:pos] + ch + s[pos+1:]

def simulateStep():
    global posx, posy, currentSymbol
    if currentSymbol == "^":
        inp[posy] = change(inp[posy], posx, "X")
        if posy == 0:
            return False
        else:
            if inp[posy-1][posx] == "#":
                currentSymbol = ">"
            else:
                posy = posy - 1
    elif currentSymbol == "v":
        inp[posy] = change(inp[posy], posx, "X")
        if posy == len(inp)-1:
            return False
        else:
            if inp[posy+1][posx] == "#":
                currentSymbol = "<"
            else:
                posy = posy + 1
    elif currentSymbol == ">":
        inp[posy] = change(inp[posy], posx, "X")
        if posx == len(inp[posy])-1:
            return False
        else:
            if inp[posy][posx+1] == "#":
                currentSymbol = "v"
            else:
                posx = posx + 1
    elif currentSymbol == "<":
        inp[posy] = change(inp[posy], posx, "X")
        if posx == 0:
            return False
        else:
            if inp[posy][posx-1] == "#":
                currentSymbol = "^"
            else:
                posx = posx - 1
    return True


while simulateStep():
    pass

for l in inp:
    result = result + l.count("X")
print(result)

#Part 2
result = 0
allOptions = []
inp = []

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

posy = -1
posx = -1
currentSymbol = "^"
for i in range(len(inp)):
    if "^" in inp[i]:
        posy = i
        posx = inp[i].index("^")
inp[posy] = change(inp[posy], posx, ".")

def simulateStepFirst(te):
    global posx, posy, currentSymbol, result
    
    if te:
        if inp[posy][posx] == currentSymbol:
            result = result + 1
            return False
    else:
        allOptions.append((posy, posx))
        
    if currentSymbol == "^":
        inp[posy] = change(inp[posy], posx, currentSymbol)
        if posy == 0:
            return False
        else:
            if inp[posy-1][posx] == "#":
                currentSymbol = ">"
            else:
                posy = posy - 1
    elif currentSymbol == "v":
        inp[posy] = change(inp[posy], posx, currentSymbol)
        if posy == len(inp)-1:
            return False
        else:
            if inp[posy+1][posx] == "#":
                currentSymbol = "<"
            else:
                posy = posy + 1
    elif currentSymbol == ">":
        inp[posy] = change(inp[posy], posx, currentSymbol)
        if posx == len(inp[posy])-1:
            return False
        else:
            if inp[posy][posx+1] == "#":
                currentSymbol = "v"
            else:
                posx = posx + 1
    elif currentSymbol == "<":
        inp[posy] = change(inp[posy], posx, currentSymbol)
        if posx == 0:
            return False
        else:
            if inp[posy][posx-1] == "#":
                currentSymbol = "^"
            else:
                posx = posx - 1
    return True

while simulateStepFirst(False):
    pass

allOptions = list(set(allOptions))

for i in range(len(allOptions)):
    opty, optx = allOptions[i]
    inp = []
    with open("input.txt", "r") as f:
        for line in f:
            inp.append(line.rstrip())

    posy = -1
    posx = -1
    currentSymbol = "^"
    for i in range(len(inp)):
        if "^" in inp[i]:
            posy = i
            posx = inp[i].index("^")
    inp[posy] = change(inp[posy], posx, ".")

    ori = inp[opty][optx]
    
    inp[opty] = change(inp[opty], optx, "#")
    c = 1000000 # well I am bad at detecting loops :D
    while simulateStepFirst(True):
        c = c - 1
        if c < 0:
            result = result + 1
            break
        pass
    inp[opty] = change(inp[opty], optx, ori)


#for l in inp:
    #print(l)
print(result)
