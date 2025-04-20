#import re
#from functools import cmp_to_key
#from copy import deepcopy

inp = []
result = []


with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

#Part 1
regA = int(inp[0][inp[0].index(":")+1:])
regB = int(inp[1][inp[1].index(":")+1:])
regC = int(inp[2][inp[2].index(":")+1:])
inst = [int(x) for x in inp[4][inp[4].index(":")+1:].split(",")]
ip = 0

while ip < len(inst):
    if inst[ip] == 0:
        if inst[ip+1] <= 3:
            regA = regA // 2**inst[ip+1]
        elif inst[ip+1] == 4:
            regA = regA // 2**regA
        elif inst[ip+1] == 5:
            regA = regA // 2**regB
        elif inst[ip+1] == 6:
            regA = regA // 2**regC
    elif inst[ip] == 1:
        regB = regB ^ inst[ip+1]
    elif inst[ip] == 2:
        if inst[ip+1] <= 3:
            regB = inst[ip+1]
        elif inst[ip+1] == 4:
            regB = regA % 8
        elif inst[ip+1] == 5:
            regB = regB % 8
        elif inst[ip+1] == 6:
            regB = regC % 8
    elif inst[ip] == 3:
        if regA != 0:
            ip = inst[ip+1]
            continue
    elif inst[ip] == 4:
        regB = regB ^ regC
    elif inst[ip] == 5:
        if inst[ip+1] <= 3:
            result.append(str(inst[ip+1]))
        elif inst[ip+1] == 4:
            result.append(str(regA % 8))
        elif inst[ip+1] == 5:
            result.append(str(regB % 8))
        elif inst[ip+1] == 6:
            result.append(str(regC % 8))
    elif inst[ip] == 6:
        if inst[ip+1] <= 3:
            regB = regA // pow(2, inst[ip+1])
        elif inst[ip+1] == 4:
            regB = regA // pow(2, regA)
        elif inst[ip+1] == 5:
            regB = regA // pow(2, regB)
        elif inst[ip+1] == 6:
            regB = regA // pow(2, regC)
    elif inst[ip] == 7:
        if inst[ip+1] <= 3:
            regC = regA // pow(2, inst[ip+1])
        elif inst[ip+1] == 4:
            regC = regA // pow(2, regA)
        elif inst[ip+1] == 5:
            regC = regA // pow(2, regB)
        elif inst[ip+1] == 6:
            regC = regA // pow(2, regC)
    ip += 2

print(','.join(result))

#Part 2

#mul = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#currSearch = 15
st = 164541017976448
test = inp[4][inp[4].index(":")+2:]
while True:
    regA = st
#    for k in range(16):
#        regA += (8**k)*mul[k]
#    print(regA)
#    print(mul)
    regB = int(inp[1][inp[1].index(":")+1:])
    regC = int(inp[2][inp[2].index(":")+1:])
    result = []
    ip = 0
    while ip < len(inst):
        if inst[ip] == 0:
            if inst[ip+1] <= 3:
                regA = regA // 2**inst[ip+1]
            elif inst[ip+1] == 4:
                regA = regA // 2**regA
            elif inst[ip+1] == 5:
                regA = regA // 2**regB
            elif inst[ip+1] == 6:
                regA = regA // 2**regC
        elif inst[ip] == 1:
            regB = regB ^ inst[ip+1]
        elif inst[ip] == 2:
            if inst[ip+1] <= 3:
                regB = inst[ip+1]
            elif inst[ip+1] == 4:
                regB = regA % 8
            elif inst[ip+1] == 5:
                regB = regB % 8
            elif inst[ip+1] == 6:
                regB = regC % 8
        elif inst[ip] == 3:
            if regA != 0:
                ip = inst[ip+1]
                continue
        elif inst[ip] == 4:
            regB = regB ^ regC
        elif inst[ip] == 5:
            if inst[ip+1] <= 3:
                result.append(str(inst[ip+1]))
            elif inst[ip+1] == 4:
                result.append(str(regA % 8))
            elif inst[ip+1] == 5:
                result.append(str(regB % 8))
            elif inst[ip+1] == 6:
                result.append(str(regC % 8))
        elif inst[ip] == 6:
            if inst[ip+1] <= 3:
                regB = regA // pow(2, inst[ip+1])
            elif inst[ip+1] == 4:
                regB = regA // pow(2, regA)
            elif inst[ip+1] == 5:
                regB = regA // pow(2, regB)
            elif inst[ip+1] == 6:
                regB = regA // pow(2, regC)
        elif inst[ip] == 7:
            if inst[ip+1] <= 3:
                regC = regA // pow(2, inst[ip+1])
            elif inst[ip+1] == 4:
                regC = regA // pow(2, regA)
            elif inst[ip+1] == 5:
                regC = regA // pow(2, regB)
            elif inst[ip+1] == 6:
                regC = regA // pow(2, regC)
        ip += 2
# Rough estimeate using commented code
#    compNum = "45670123"
#    print(currSearch)
#    if compNum.index(str(inst[currSearch])) == compNum.index(result[currSearch]):
#        currSearch -= 1
#    elif compNum.index(str(inst[currSearch])) != compNum.index(result[currSearch]):
#        mul[currSearch] += 1
#        mul[currSearch] = mul[currSearch]
    
    if (test == ','.join(result)):
        print(st)
        break
    st += 1
