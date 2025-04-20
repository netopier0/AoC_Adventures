#import re
#from functools import cache, cmp_to_key
#from copy import deepcopy
#from collections import deque

inp = []
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

#Part 1
def numToKey(nums):
    coords = {"7": (0,0), "8":(0,1), "9":(0,2),
              "4": (1,0), "5":(1,1), "6":(1,2),
              "1": (2,0), "2":(2,1), "3":(2,2),
                          "0":(3,1), "A":(3,2)}
    res = ""
    currY = 3
    currX = 2
    for n in nums:
        #Hover Over invalid check
        if currY == 3 and coords[n][1] == 0 or currX == 0 and coords[n][0] == 3:
            if coords[n][0] < currY:
                res += "^"*(currY - coords[n][0])
            if coords[n][1] < currX:
                res += "<"*(currX - coords[n][1])
            if coords[n][1] > currX:
                res += ">"*(coords[n][1] - currX)
            if coords[n][0] > currY:
                res += "v"*(coords[n][0] - currY)
        else:
            if coords[n][1] < currX:
                res += "<"*(currX - coords[n][1])
            if coords[n][0] < currY:
                res += "^"*(currY - coords[n][0])
            if coords[n][0] > currY:
                res += "v"*(coords[n][0] - currY)
            if coords[n][1] > currX:
                res += ">"*(coords[n][1] - currX)
        res += "A"
        currY, currX = coords[n]
    return res

def keyToKey(keys):
    coords = {            "^":(0,1), "A":(0,2),
              "<": (1,0), "v":(1,1), ">":(1,2)}
    res = ""
    currY = 0
    currX = 2
    for k in keys:
        #Hover Over invalid check
        if currY == 0 and coords[k][1] == 0 or currX == 0 and coords[k][0] == 0:
            if coords[k][0] > currY:
                res += "v"*(coords[k][0] - currY)
            if coords[k][1] < currX:
                res += "<"*(currX - coords[k][1])
            if coords[k][1] > currX:
                res += ">"*(coords[k][1] - currX)
            if coords[k][0] < currY:
                res += "^"*(currY - coords[k][0])

        else:   
            if coords[k][1] < currX:
                res += "<"*(currX - coords[k][1])
            if coords[k][0] < currY:
                res += "^"*(currY - coords[k][0])
            if coords[k][0] > currY:
                res += "v"*(coords[k][0] - currY)
            if coords[k][1] > currX:
                res += ">"*(coords[k][1] - currX)
        res += "A"
        currY, currX = coords[k]
    return res

for l in inp:
    result += len(keyToKey(keyToKey(numToKey(l)))) * int(l[:-1])
print(result)

#Part 2
result = 0

for l in inp:
    keysOrder = numToKey(l)
    used = {}
    for kO in keysOrder.split("A")[:-1]:
        if kO + "A" not in used:
            used[kO + "A"] = 0
        used[kO + "A"] += 1

    for i in range(26):
        newUsed = {}
        for usedKey in used.keys():
            nextKeys = keyToKey(usedKey)
            for nK in nextKeys.split("A")[:-1]:
                if nK + "A" not in newUsed:
                    newUsed[nK + "A"] = 0
                newUsed[nK + "A"] += used[usedKey]
        used = newUsed
        
    for usedKey in used.keys():
        result += used[usedKey] * int(l[:-1])

print(result)

