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
def nextNum(n):
    n = n ^ n*64
    n = n%16777216
    n = n ^ n//32
    n = n%16777216
    n = n ^ n*2048
    n = n%16777216
    return n


for l in inp:
    n = int(l)
    for i in range(2000):
        n = nextNum(n)
    result += n
print(result)

#Part 2
totalGain = dict()
for l in inp:
    n = int(l)
    pr = dict()
    difs = []
    for i in range(2000):
        tmp_n = nextNum(n)
        difs.append(int(str(tmp_n)[-1]) - int(str(n)[-1]))
        n = tmp_n
        if len(difs) > 4:
            if (difs[-4], difs[-3], difs[-2], difs[-1]) not in pr:
                pr[(difs[-4], difs[-3], difs[-2], difs[-1])] = int(str(n)[-1])

    for prKey in pr.keys():
        if prKey not in totalGain:
            totalGain[prKey] = 0
        totalGain[prKey] += pr[prKey]

print(max(totalGain.values()))
