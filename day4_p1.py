import sys

def findXMAS(xX: int, xY: int, crossword: list[str]) -> int:
    maxX = len(crossword[0])
    maxY = len(crossword)
    
    hits = 0
    # left
    if xX >= 3:
        found = ''
        for step in range(1,4):
            found += crossword[xY][xX-step]
        if found == "MAS":
            hits+=1

    # right
    if xX + 3 < maxX:
        found = ''
        for step in range(1,4):
            found += crossword[xY][xX+step]
        if found == "MAS":
            hits+=1

    # up
    if xY >= 3:
        found = ''
        for step in range(1,4):
            found += crossword[xY-step][xX]
        if found == "MAS":
            hits+=1

    # down
    if xY + 3 < maxY:
        found = ''
        for step in range(1,4):
            found += crossword[xY+step][xX]
        if found == "MAS":
            hits+=1

    # diag left-up
    if xX >= 3 and xY >= 3:
        found = ''
        for step in range(1,4):
            found += crossword[xY-step][xX-step]
        if found == "MAS":
            hits+=1

    # diag left-down
    if xX >= 3 and xY + 3 < maxY:
        found = ''
        for step in range(1,4):
            found += crossword[xY+step][xX-step]
        if found == "MAS":
            hits+=1

    # diag right-up
    if xX + 3 < maxX and xY >= 3:
        found = ''
        for step in range(1,4):
            found += crossword[xY-step][xX+step]
        if found == "MAS":
            hits+=1

    # diag right-down
    if xX + 3 < maxX and xY + 3 < maxY:
        found = ''
        for step in range(1,4):
            found += crossword[xY+step][xX+step]
        if found == "MAS":
            hits+=1

    return hits

# main
if len(sys.argv) > 1 and sys.argv[1] == '-sample':
    file = open("day4_sample.in", "r")
else:
    file = open("day4.in", "r")

crossword = file.readlines()
crossword = [row.rstrip('\n') for row in crossword]

maxX = len(crossword[0])
maxY = len(crossword)
hits = 0
for y in range(maxY):
    for x in range(maxX):
        if crossword[y][x] == "X":
            hits += findXMAS(x, y, crossword)

print("# of XMAS: " + str(hits))