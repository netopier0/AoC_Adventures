inp = []
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())

inA = []
inB = []
for l in inp:
    a, b = l.split()
    inA.append(int(a))
    inB.append(int(b))

inA.sort()
inB.sort()

#Part 1
for i in range(0, len(inA)):
    result = result + abs(inA[i] - inB[i])

print(result)

#Part 2
result = 0
inBCount = {}
for i in range(0, len(inB)):
    if inB[i] not in inBCount:
        inBCount[inB[i]] = 1
    else:
        inBCount[inB[i]] = inBCount[inB[i]] + 1

for i in range(0, len(inA)):
    if inA[i] in inBCount:
        result = result + inA[i] * inBCount[inA[i]]

print(result)
