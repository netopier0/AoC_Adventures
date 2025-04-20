import re
inp = ""
result = 0

with open("input.txt", "r") as f:
    for line in f:
        inp = inp + line
#Part 1
for m in re.findall("mul\([0-9]+,[0-9]+\)", inp):
    p = re.search("([0-9]+,)([0-9]+)",m)
    a = int(p.group(1)[:-1])
    b = int(p.group(2))
    if a > 999 or b > 999:
        continue
    result = result + a * b

print(result)

#Part 2
result = 0
en = True
for m in re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", inp):
    if m[0] == "d":
        if m[2] == "n":
            en = False
        else:
            en = True
        continue
    p = re.search("([0-9]+,)([0-9]+)",m)
    a = int(p.group(1)[:-1])
    b = int(p.group(2))
    if a > 999 or b > 999:
        continue
    if en:
        result = result + a * b

print(result)
