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
locks = dict()
keys = dict()

for i in range(6):
    for j in range(5):
        locks[(j,i)] = set()
        keys[(j,i)] = set()

for i in range((len(inp)+1)//8):
    c = [0,0,0,0,0]
    for j in range(1,6):
        for k in range(5):
            if inp[8*i+j][k] == "#":
                c[k] += 1
    if inp[8*i] == "#####":
        for i in range(5):
            locks[(i,c[i])].add((c[0],c[1],c[2],c[3],c[4]))
    elif inp[8*i+6] == "#####":
        for i in range(5):
            keys[(i,c[i])].add((c[0],c[1],c[2],c[3],c[4]))

def getAllFitKeys(lock):
    pins = [set(), set(), set(), set(), set()]
    for i in range(5):
        for n in range(6-lock[i]):
            pins[i] = pins[i].union(keys[(i, n)])
    return pins[0].intersection(pins[1]).intersection(pins[2]).intersection(pins[3]).intersection(pins[4])


for i in range(6):
    for lock in locks[(0,i)]:
        result += len(getAllFitKeys(lock))

print(result)
