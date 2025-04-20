#import re
#from functools import cmp_to_key
#from copy import deepcopy
import sys
sys.setrecursionlimit(10000)

inp = []
result = 0
bestScores = [[],[],[],[]]

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())
        bestScores[0].append([-1]*len(inp[-1]))
        bestScores[1].append([-1]*len(inp[-1]))
        bestScores[2].append([-1]*len(inp[-1]))
        bestScores[3].append([-1]*len(inp[-1]))


y = 0
x = 0
tarY = 0
tarX = 0


for i in range(len(inp)):
    if "S" in inp[i]:
        y = i
        x = inp[i].index("S")
    if "E" in inp[i]:
        tarY = i
        tarX = inp[i].index("E")

#Part 1

#D = North, East, South, West
def traverse(path, score, y, x, d, targetY, targetX):
    #This if is here because I alredy found right answer and didn't want to wait for minutes until I find it again for Part 2
    if score > 79500:
        return
    
    if bestScores[d][y][x] != -1 and score >= bestScores[d][y][x]:
        return
    else:
        bestScores[d][y][x] = score
    if y == targetY and x == targetX:
        #print(score)
        #print(bestScores[0][y][x], bestScores[1][y][x], bestScores[2][y][x], bestScores[3][y][x])
        return
    
    for i in [-1, 1, 0]:
        newd = (d+i)%4
        newS = score+1
        if i != 0:
            newS += 1000
        if newd == 0:
            if inp[y-1][x] != "#" and (y-1, x) not in path:
                traverse(path + [(y, x)], newS, y-1, x, newd, targetY, targetX)

        if newd == 1:
            if inp[y][x+1] != "#" and (y, x+1) not in path:
                traverse(path + [(y, x)], newS, y, x+1, newd, targetY, targetX)

        if newd == 2:
            if inp[y+1][x] != "#" and (y+1, x) not in path:
                traverse(path + [(y, x)], newS, y+1, x, newd, targetY, targetX)

        if newd == 3:
            if inp[y][x-1] != "#" and (y, x-1) not in path:
                traverse(path + [(y, x)], newS, y, x-1, newd, targetY, targetX)

#Slow but works
traverse([], 0, y, x, 1, tarY, tarX)
for i in range(4):
    if bestScores[i][tarY][tarX] != -1:
        if result == 0:
            result = bestScores[i][tarY][tarX]
        else:
            result = min(result, bestScores[i][tarY][tarX])
print(result)

#Part 2
allSeen = {(y, x), (tarY, tarX)}

def traverseSecond(prevRes, path, score, y, x, d, targetY, targetX):

    if bestScores[d][y][x] == -1 or score > bestScores[d][y][x]:
        return

    if y == targetY and x == targetX and score == prevRes:
        global allSeen
        allSeen = allSeen.union(set(path))
        return
    
    for i in [-1, 1, 0]:
        newd = (d+i)%4
        newS = score+1
        if i != 0:
            newS += 1000
        if newd == 0:
            if inp[y-1][x] != "#" and (y-1, x) not in path:
                traverseSecond(prevRes, path + [(y, x)], newS, y-1, x, newd, targetY, targetX)

        if newd == 1:
            if inp[y][x+1] != "#" and (y, x+1) not in path:
                traverseSecond(prevRes, path + [(y, x)], newS, y, x+1, newd, targetY, targetX)

        if newd == 2:
            if inp[y+1][x] != "#" and (y+1, x) not in path:
                traverseSecond(prevRes, path + [(y, x)], newS, y+1, x, newd, targetY, targetX)

        if newd == 3:
            if inp[y][x-1] != "#" and (y, x-1) not in path:
                traverseSecond(prevRes, path + [(y, x)], newS, y, x-1, newd, targetY, targetX)

traverseSecond(result, [], 0, y, x, 1, tarY, tarX)

print(len(allSeen))






