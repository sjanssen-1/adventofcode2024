import sys
import re

if len(sys.argv) > 1 and sys.argv[1] == '-sample':
    file = open("day3_sample.in", "r")
else:
    file = open("day3.in", "r")

result = 0
mulenabled = True
for line in file:
    index = 0

    while index >= 0:
        line = line[index:]
        mulfind = re.search(r"mul\((\d*),(\d*)\)", line)
        if mulfind == None:
            break
        mulindex = mulfind.end()
        dofind = re.search(r"do\(\)", line)
        if dofind == None:
            doindex = sys.maxsize
        else:
            doindex = re.search(r"do\(\)", line).end()

        dontfind = re.search(r"don't\(\)", line)
        if dontfind == None:
            dontindex = sys.maxsize
        else:
            dontindex = re.search(r"don't\(\)", line).end()

        if mulindex < doindex and mulindex < dontindex:
            if mulenabled:
                result += int(mulfind.groups()[0]) * int(mulfind.groups()[1])
            index = mulindex
        elif doindex < mulindex and doindex < dontindex:
            mulenabled = True
            index = doindex
        else:
            mulenabled = False
            index = dontindex

print(result)