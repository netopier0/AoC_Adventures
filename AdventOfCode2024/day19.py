#import re
from functools import cache#, cmp_to_key
#from copy import deepcopy
#from collections import deque

inp = []
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

patterns = set(inp[0].split(", "))

#Part 1

# cache - hint from reddit
@cache
def testPattern(pat):
    if len(pat) == 0:
        return True
    
    for i in range(8): # 8 is the longest pattern
        if pat[:i] in patterns:
            if testPattern(pat[i:]):
                return True
            
    return False

for i in range(2, len(inp)):
    if testPattern(inp[i]):
        result += 1

print(result)

#Part 2
result = 0

@cache
def testPattern(pat):
    if len(pat) == 0:
        return 1
    res = 0

    for p in patterns:
        if len(p) <= len(pat):
            if pat[:len(p)] == p:
                res += testPattern(pat[len(p):])
            
    return res

for i in range(2, len(inp)):
    result += testPattern(inp[i])

print(result)
