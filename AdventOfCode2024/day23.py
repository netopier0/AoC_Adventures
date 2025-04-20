#import re
#from functools import cache, cmp_to_key
from copy import deepcopy
#from collections import deque

inp = []
result = []

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

#Part 1
conn = dict()

for l in inp:
    a = l[:l.index("-")]
    b = l[l.index("-")+1:]
    if a not in conn:
        conn[a] = []
    conn[a].append(b)
    if b not in conn:
        conn[b] = []
    conn[b].append(a)

triples = set()

for key in conn.keys():
    if key[0] == "t":
        for i in range(len(conn[key])):
            for j in range(i+1,len(conn[key])):
                if conn[key][i] in conn[conn[key][j]]:
                    triples.add("".join(sorted([key, conn[key][i], conn[key][j]])))

print(len(triples))
        
#Part 2

def getBiggestConnectedSize(ver):
    full = deepcopy(conn[ver]) #Reddit helped, needed to use deepcopy otherwise remove was messing with list in dictionary
    i = 0
    while i <= len(full):
        for el in full[i+1:]:
            if el not in conn[full[i]]:
                i -= 1
                full.remove(full[i])
                break
        i += 1
    return (len(full) + 1, [ver] + full)

maxSize = 0
for key in conn.keys():
    s, tmpRes = getBiggestConnectedSize(key)
    if max(maxSize, s) != maxSize:
        result = tmpRes
        maxSize = s
        
print(",".join(sorted(result)))
