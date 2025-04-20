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
states = dict()
transitions = dict()
statesDone = False

for l in inp:
    if l == "":
        statesDone = True
        continue
    splt = l.split(" ")
    if not statesDone:
        states[splt[0][:-1]] = int(splt[1]) == 1

    if statesDone:
        transitions[splt[4]] = (splt[0], splt[1], splt[2])

def eval(val):
    if val in states:
        return
    a, op, b = transitions[val]
    #Print for part 2
    #print(a + " -> " + val + " " +  '[ label = "' + op + '" ];')
    #print(b + " -> " + val + " " +  '[ label = "' + op + '" ];')
    if a not in states:
        eval(a)
    if b not in states:
        eval(b)

    if op == "AND":
        states[val] = states[a] and states[b]
    elif op == "OR":
        states[val] = states[a] or states[b]
    elif op == "XOR":
        states[val] = (states[a] or states[b]) and not(states[a] and states[b])
    else:
        print("Unknown opcode: " + op)

highest = 0

for key in transitions.keys():
    if key[0] == "z":
        eval(key)
        highest = max(highest, int(key[1:]))

for i in range(highest, -1, -1):
    result *= 2
    if i < 10:
        result += int(states["z0" + str(i)])
    else:
        result += int(states["z" + str(i)])
print(result)

#Part 2
states = dict()
transitions = dict()
statesDone = False

for l in inp:
    if l == "":
        statesDone = True
        continue
    splt = l.split(" ")
    if not statesDone:
        states[splt[0][:-1]] = int(splt[1]) == 1

    if statesDone:
        transitions[splt[4]] = (splt[0], splt[1], splt[2])

#Done by hand using Webgraphviz after hint from reddit (did not know what Ripple-carry adder was before)
transitions["z05"], transitions["gdd"] = transitions["gdd"], transitions["z05"]
transitions["z09"], transitions["cwt"] = transitions["cwt"], transitions["z09"]
transitions["css"], transitions["jmv"] = transitions["jmv"], transitions["css"]
transitions["z37"], transitions["pqt"] = transitions["pqt"], transitions["z37"]

for key in transitions.keys():
    eval(key)

res = 0
for i in range(45):
    if i < 10:
        res += int(states["x0" + str(i)]) + int(states["y0" + str(i)])
        if res % 2 != int(states["z0" + str(i)]):
            print("Error " + "z0" + str(i))
        res //= 2
    else:
        res += int(states["x" + str(i)]) + int(states["y" + str(i)])
        if res % 2 != int(states["z" + str(i)]):
            print("Error " + "z" + str(i))
        res //= 2
    if i == 44:
        if res != int(states["z45"]):
            print("Error " + "z45")

print(",".join(sorted(["z05", "gdd", "z09", "cwt", "css", "jmv", "z37", "pqt"])))
