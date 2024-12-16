import sys
from typing import List, Dict

def findStart(map: list[str]):
    xl = len(map[0])
    yl = len(map)
    for y in range(yl):
        for x in range(xl):
            if map[y][x] == '^':
                return x, y

def changeDirection(direction: str):
    match direction:
        case "up":
            return "right"
        case "right":
            return "down"
        case "down":
            return "left"
        case "left":
            return "up"

# main
if len(sys.argv) > 1 and sys.argv[1] == '-real':
    file = open("day6.in", "r")
else:
    file = open("day6_sample.in", "r")

map = file.readlines()
map = [row.rstrip('\n') for row in map]

start = findStart(map)

x = start[0]
y = start[1]
current_direction = "up"
locations = set()

while x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
    pos = map[y][x]

    if pos == "#":
        if current_direction == "up":
            y+=1
        elif current_direction == "right":
            x-=1
        elif current_direction == "down":
            y-=1
        else: # left
            x+=1
        current_direction = changeDirection(current_direction)
        continue
    
    locations.add((x,y))

    if current_direction == "up":
        y-=1
    elif current_direction == "right":
        x+=1
    elif current_direction == "down":
        y+=1
    else: # left
        x-=1

print("distinct locations: " + str(len(locations)))