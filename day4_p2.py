import sys

def findXMAS(aX: int, aY: int, crossword: list[str]) -> bool:
    maxX = len(crossword[0])
    maxY = len(crossword)
    
    strike1 = False
    strike2 = False

    # diag lu to rd
    if (aX >= 1 and aY >=1) and (aX+1 < maxX and aY+1 < maxY):
        found = crossword[aY-1][aX-1]
        found += crossword[aY][aX]
        found += crossword[aY+1][aX+1]
        strike1 = found == "SAM" or found == "MAS"

    # diag ld to ru
    if (aX >= 1 and aY + 1 < maxY) and (aX + 1 < maxX and aY >= 1):
        found = crossword[aY+1][aX-1]
        found += crossword[aY][aX]
        found += crossword[aY-1][aX+1]
        strike2 = found == "SAM" or found == "MAS"

    return strike1 and strike2

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
        if crossword[y][x] == "A":
            if findXMAS(x,y,crossword):
                hits+=1

print("# of X-MAS: " + str(hits))