inp = []
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.rstrip())


def testValid(row):
    safe = True        
    if row != sorted(row) and row != sorted(row)[::-1]:
        safe = False
    curr = row[0]
    for i in range(1, len(row)):
        if not safe:
            break
        diff = abs(curr - row[i])
        if diff == 1 or diff == 2 or diff == 3:
            pass
        else:
            safe = False
            break
        curr = row[i]
    return safe

#Part 1
for l in inp:
    row = [int(item) for item in l.split()]
    safe = testValid(row)
    if safe:
        result = result + 1

print(result)

#Part 2
result = 0

for l in inp:
    row = [int(item) for item in l.split()]
    allSafe = []
    for i in range(len(row)):
        allSafe.append(testValid(row[:i] + row[i+1:]))
    if any(allSafe):
        result = result + 1

print(result)
