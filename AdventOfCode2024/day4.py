#import re
inp = []
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

#Part 1

def checkInDir(posy, posx, diry, dirx):
    letters = ["X", "M", "A", "S"]
    if 0 > posy + 3*diry or posy + 3*diry >= len(inp) or 0 > posx + 3*dirx or posx + 3*dirx >= len(inp[posy]):
        return 0
    for i in range(4):
        if letters[i] != inp[posy + i*diry][posx + i*dirx]:
            return 0
    return 1

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == "X":
            for a in [-1, 0, 1]:
                for b in [-1, 0 , 1]:
                    result = result + checkInDir(i, j, a, b)
print(result)

#Part 2
result = 0

def checkForX(posy, posx):
    if 1 > posy or posy >= len(inp)-1 or 1 > posx or posx >= len(inp[posy])-1:
        return 0
    if inp[posy-1][posx-1] == inp[posy+1][posx+1] or inp[posy+1][posx-1] == inp[posy-1][posx+1]:
        return 0
    r = {"X": 0, "M": 0, "A": 0, "S": 0}
    r[inp[posy-1][posx-1]] += 1
    r[inp[posy+1][posx-1]] += 1
    r[inp[posy-1][posx+1]] += 1
    r[inp[posy+1][posx+1]] += 1
    if r["M"] == 2 and r["S"] == 2:
        return 1
    return 0

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == "A":
            result = result + checkForX(i, j)
print(result)
